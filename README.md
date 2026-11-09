
** EventFlow

EventFlow is a simple web application for event registration.

Organizers can create events and see registrations. Visitors can view events and register without an account.

** Technologies

- Frontend: HTML, CSS, Bootstrap
- Backend: Python, Flask
- Database: PostgreSQL

** Features

- View events
- Create events
- Register for events
- Check available places
- View registrations
- Cancel registrations
- Organizer and admin login

** Run locally

1. Install Python and PostgreSQL.
2. Create a database named `eventflow`.
3. Create a `.env` file with database settings.
4. Open the project in VS Code.
5. Open a terminal in the `backend` folder.
6. Create a virtual environment: `python -m venv .venv`
7. Activate it in Git Bash: `source .venv/Scripts/activate`
8. Install dependencies: `pip install -r requirements.txt`
9. Create database tables: `flask --app app init-db`
10. Create an organizer: `flask --app app create-organizer`
11. Start the application: `python app.py`
12. Open the application in a browser.

** Documentation

- [Project idea](docs/01-zasnova-resitve.md)
- [Features](docs/02-funkcionalnosti-in-obseg.md)
- [Data model](docs/03-podatkovni-model.md)
- [Architecture](docs/04-arhitektura-in-tehnoloski-sklad.md)
- [User stories](docs/05-uporabniske-zgodbe.md)
- [Wireframes](docs/06-wireframes.md)
