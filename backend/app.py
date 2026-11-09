"""EventFlow MVP – Flask routes, PostgreSQL data and basic login."""
import os
from datetime import datetime
from functools import wraps

import click
import psycopg
from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from psycopg.rows import dict_row
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()
app = Flask(__name__, template_folder="templates", static_folder="../frontend/static")
app.secret_key = os.getenv("SECRET_KEY", "")
if not app.secret_key or app.secret_key == "replace-with-a-long-random-value":
    raise RuntimeError("Set SECRET_KEY in EventFlow/.env before starting the app.")


def db():
    """Open a PostgreSQL connection that returns dictionary-like rows."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("Set DATABASE_URL in the .env file first.")
    return psycopg.connect(url, row_factory=dict_row)


def current_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None
    with db() as conn:
        user = conn.execute("SELECT id, name, role, active FROM users WHERE id = %s", (user_id,)).fetchone()
    return user if user and user["active"] else None


@app.context_processor
def inject_user():
    return {"current_user": current_user(), "now": datetime.now}


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if current_user() is None:
            flash("Please log in first.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def owned_event(event_id):
    """Find an event that this organizer is allowed to manage."""
    user = current_user()
    if not user:
        abort(403)
    with db() as conn:
        event = conn.execute("SELECT * FROM events WHERE id = %s", (event_id,)).fetchone()
    if not event or (user["role"] != "admin" and event["organizer_id"] != user["id"]):
        abort(404)
    return event


@app.get("/")
def home():
    with db() as conn:
        events = conn.execute("""
            SELECT e.*, e.capacity - COUNT(r.id) AS free_places
            FROM events e
            LEFT JOIN registrations r ON r.event_id=e.id AND r.status='active'
            WHERE e.is_public=TRUE AND e.date >= CURRENT_TIMESTAMP
            GROUP BY e.id ORDER BY e.date
        """).fetchall()
    return render_template("home.html", events=events)


@app.get("/events/<int:event_id>")
def event_details(event_id):
    with db() as conn:
        event = conn.execute("""
            SELECT e.*, e.capacity - COUNT(r.id) AS free_places
            FROM events e
            LEFT JOIN registrations r ON r.event_id=e.id AND r.status='active'
            WHERE e.id=%s AND e.is_public=TRUE
            GROUP BY e.id
        """, (event_id,)).fetchone()
    if event is None:
        abort(404)
    return render_template("event.html", event=event)


@app.post("/events/<int:event_id>/register")
def register(event_id):
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    if not name or len(name) > 100 or len(email) > 254 or "@" not in email or "." not in email.split("@")[-1]:
        flash("Enter your name and a valid email.", "error")
        return redirect(url_for("event_details", event_id=event_id))

    with db() as conn:
        # Lock event row: simultaneous requests cannot exceed capacity.
        event = conn.execute("SELECT * FROM events WHERE id=%s FOR UPDATE", (event_id,)).fetchone()
        if not event or not event["is_public"]:
            abort(404)
        if event["date"] < datetime.now():
            flash("This event has already started.", "error")
        elif conn.execute("""SELECT 1 FROM registrations WHERE event_id=%s
                             AND LOWER(participant_email)=%s AND status='active'""",
                          (event_id, email)).fetchone():
            flash("This email is already registered.", "error")
        else:
            count = conn.execute("""SELECT COUNT(*) AS total FROM registrations
                                  WHERE event_id=%s AND status='active'""", (event_id,)).fetchone()["total"]
            if count >= event["capacity"]:
                flash("This event is full.", "error")
            else:
                conn.execute("""INSERT INTO registrations (event_id, participant_name, participant_email)
                                VALUES (%s, %s, %s)""", (event_id, name, email))
                flash("Registration successful!", "success")
    return redirect(url_for("event_details", event_id=event_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        with db() as conn:
            user = conn.execute("SELECT * FROM users WHERE LOWER(email)=%s", (email,)).fetchone()
        if user and user["active"] and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("dashboard"))
        flash("Incorrect email or password.", "error")
    return render_template("login.html")


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.get("/dashboard")
@login_required
def dashboard():
    user = current_user()
    with db() as conn:
        if user["role"] == "admin":
            events = conn.execute("SELECT * FROM events ORDER BY date").fetchall()
        else:
            events = conn.execute("SELECT * FROM events WHERE organizer_id=%s ORDER BY date", (user["id"],)).fetchall()
    return render_template("dashboard.html", events=events)


@app.route("/events/new", methods=["GET", "POST"])
@login_required
def create_event():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        location = request.form.get("location", "").strip()
        description = request.form.get("description", "").strip()
        date_text = request.form.get("date", "")
        try:
            date = datetime.fromisoformat(date_text)
            capacity = int(request.form.get("capacity", "0"))
            valid = bool(title and location and capacity > 0 and date > datetime.now())
        except (ValueError, TypeError):
            valid = False
        if not valid:
            flash("Enter a title, location, future date and positive capacity.", "error")
        else:
            with db() as conn:
                conn.execute("""INSERT INTO events (organizer_id, title, description, date, location, capacity)
                                VALUES (%s, %s, %s, %s, %s, %s)""",
                             (current_user()["id"], title, description, date, location, capacity))
            flash("Event created.", "success")
            return redirect(url_for("dashboard"))
    return render_template("new_event.html")


@app.get("/manage/<int:event_id>")
@login_required
def manage(event_id):
    event = owned_event(event_id)
    with db() as conn:
        registrations = conn.execute("""SELECT * FROM registrations
                                        WHERE event_id=%s ORDER BY id""", (event_id,)).fetchall()
    return render_template("manage.html", event=event, registrations=registrations)


@app.post("/registrations/<int:reg_id>/cancel")
@login_required
def cancel_registration(reg_id):
    with db() as conn:
        registration = conn.execute("SELECT * FROM registrations WHERE id=%s", (reg_id,)).fetchone()
        if not registration:
            abort(404)
        event_id = registration["event_id"]
        user = current_user()
        event = conn.execute("SELECT * FROM events WHERE id=%s", (event_id,)).fetchone()
        if user["role"] != "admin" and event["organizer_id"] != user["id"]:
            abort(403)
        conn.execute("UPDATE registrations SET status='cancelled' WHERE id=%s", (reg_id,))
    flash("Registration cancelled. One place is free again.", "success")
    return redirect(url_for("manage", event_id=event_id))


@app.cli.command("init-db")
def init_db():
    """Create database tables (first create the database in pgAdmin)."""
    with db() as conn:
        with open(os.path.join(os.path.dirname(__file__), "schema.sql"), encoding="utf-8") as f:
            for statement in f.read().split(";"):
                if statement.strip():
                    conn.execute(statement)
    click.echo("Database tables created.")


@app.cli.command("create-admin")
@click.option("--email", prompt=True)
@click.option("--name", prompt=True)
@click.password_option()
def create_admin(email, name, password):
    """Create the first admin account using a hashed password."""
    with db() as conn:
        conn.execute("""INSERT INTO users (name, email, password_hash, role)
                        VALUES (%s, %s, %s, 'admin')""",
                     (name, email.strip().lower(), generate_password_hash(password)))
    click.echo("Admin account created.")


@app.cli.command("create-organizer")
@click.option("--email", prompt=True)
@click.option("--name", prompt=True)
@click.password_option()
def create_organizer(email, name, password):
    """Create an organizer login for the demo."""
    with db() as conn:
        conn.execute("""INSERT INTO users (name, email, password_hash, role)
                        VALUES (%s, %s, %s, 'organizer')""",
                     (name, email.strip().lower(), generate_password_hash(password)))
    click.echo("Organizer account created.")


if __name__ == "__main__":
    app.run(debug=True)
