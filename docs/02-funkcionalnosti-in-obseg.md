 EventFlow - Features and Scope

 User roles

| Role | Can do | Cannot do |
| Visitor / participant | See public events and register with name and email | Create events, see other people's registrations, manage users |
| Organizer | Log in, create and manage own events, see and cancel registrations for own events | Manage other organizers' events or user accounts |
| Admin | Log in, manage organizer accounts and all events | See users' original passwords |

A visitor does not need an account. Only organizers and admins log in. 

Planned features

| ID | Feature | Version |
| F01 | Show a list of upcoming events | **MVP** |
| F02 | Show event details and free places | **MVP** |
| F03 | Organizer creates an event with date, location and capacity | **MVP** |
| F04 | Visitor registers for an event using name and email | **MVP** |
| F05 | Check free places and stop duplicate active registrations | **MVP** |
| F06 | Organizer sees registrations and cancels one, freeing a place | **MVP** |
| F07 | Organizer edits their event information | Planned |
| F08 | Organizer hides an event from the public list | Planned |
| F09 | Search events by name | Planned |
| F10 | Filter events by date | Planned |
| F11 | Organizer sees the number of registrations per event | Planned |
| F12 | Admin creates or disables organizer accounts | Planned |


Possible future upgrades
1. Email confirmation.
2. Waiting list for full events.
3. QR code check-in.
4. Event calendar view.
5. Download registrations as CSV.

Out of scope (not part of this project)
- Online payments and tickets.
- Video meetings or live streaming.
- Automatic certificates.
- Mobile app (Android/iOS).

Main process:
Organizer creates event > Visitor chooses event > Visitor enters details > System checks capacity and duplicates > System saves the registration > Organizer views registrations.