03 - Data Model

Entities

1. Users
- id (Primary Key)
- name
- email
- password_hash
- role

2. Events
- id (Primary Key)
- title
- date
- capacity
- organizer_id (Foreign Key)

3. Registrations
- id (Primary Key)
- event_id (Foreign Key)
- name
- email


Relationships

- One user can organize many events.
- One event can have many registrations.
- Each registration belongs to one event.