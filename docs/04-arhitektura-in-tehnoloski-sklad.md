
EventFlow - Architecture and Technologies

Main parts

- **Frontend:** Shows event pages and forms.
- **Backend:** Processes requests and connects to the database.
- **Database:** Stores users, events and registrations.

Communication

The browser sends a request to Flask. Flask communicates with PostgreSQL and returns an HTML page.

Architecture diagram

    Browser (HTML, CSS, Bootstrap)
                |
                v
          Python Flask
                |
                v
           PostgreSQL

Technology stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Login:** Flask sessions and password hashes
- **Development:** VS Code, Python, pgAdmin
- **Database connection:** psycopg

Login and permissions

- Visitors can see events and register without an account.
- Organizers and admins log in with email and password.
- Passwords are stored as hashes.
- Flask sessions remember logged-in users.
- Organizers can manage only their own events.
- Admins can manage user accounts.

Run locally

1. Install Python and PostgreSQL.
2. Create a database named `eventflow`.
3. Open the project in VS Code.
4. Create a Python virtual environment.
5. Install Flask and psycopg.
6. Set the database connection and secret key.
7. Create the tables and run Flask.
8. Open the application in a browser.


Why this architecture?

- Flask is simple and easy to learn.
- PostgreSQL stores the data.
- Bootstrap helps create a clean design.
