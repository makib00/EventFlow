# EventFlow - User Stories


## US-01 - Show upcoming events
- **Related feature:** F01 (MVP)
- **Role:** Visitor
- **User story:** As a visitor, I want to see upcoming events so I can choose an event to attend.
- **Acceptance criteria:**
  1. The page shows events that have not ended.
  2. Each event shows its name and date.
  3. If there are no events, the page shows "No events".

## US-02 - Show event details
- **Related feature:** F02 (MVP)
- **Role:** Visitor
- **User story:** As a visitor, I want to see the details of an event so I can know where and when it happens.
- **Acceptance criteria:**
  1. The page shows the event name, date and location.
  2. The page shows the number of free places.
  3. The page has a registration button.

## US-03 - Create an event
- **Related feature:** F03 (MVP)
- **Role:** Organizer
- **User story:** As an organizer, I want to create an event so I can invite people to my workshop.
- **Acceptance criteria:**
  1. The organizer enters a name, date, location and capacity.
  2. Capacity must be a positive whole number.
  3. The new event is saved and appears in the event list.

## US-04 - Register for an event
- **Related feature:** F04 (MVP)
- **Role:** Visitor
- **User story:** As a visitor, I want to register for an event so I can reserve a place.
- **Acceptance criteria:**
  1. The visitor enters a name and a valid email address.
  2. The visitor can submit the form when places are available.
  3. After a successful registration, the page shows a confirmation message.

## US-05 - Check places and duplicate registrations
- **Related feature:** F05 (MVP)
- **Role:** Visitor
- **User story:** As a visitor, I want to know whether my registration is possible so I can avoid invalid registrations.
- **Acceptance criteria:**
  1. The system does not accept a registration if the event is full.
  2. The same email cannot have two active registrations for one event.
  3. The system displays a clear message if registration is rejected.

## US-06 - View and cancel registrations
- **Related feature:** F06 (MVP)
- **Role:** Organizer
- **User story:** As an organizer, I want to view and cancel registrations for my events so I can manage available places.
- **Acceptance criteria:**
  1. The organizer can see the name and email of each registered visitor for their own event.
  2. The organizer can cancel a registration for their own event.
  3. After cancellation, the number of free places increases by one.

## US-07 - Edit an event
- **Related feature:** F07 (Planned)
- **Role:** Organizer
- **User story:** As an organizer, I want to change my event details so I can correct mistakes.
- **Acceptance criteria:**
  1. The organizer can edit the name, date and location of their own event.
  2. The organizer cannot edit another organizer's event.
  3. Saved changes appear on the event details page.

## US-08 - Hide an event
- **Related feature:** F08 (Planned)
- **Role:** Organizer
- **User story:** As an organizer, I want to hide my event so I can stop showing it to visitors.
- **Acceptance criteria:**
  1. The organizer can mark their event as hidden.
  2. Hidden events do not appear in the public event list.
  3. The organizer can still see their hidden events.

## US-09 - Search events
- **Related feature:** F09 (Planned)
- **Role:** Visitor
- **User story:** As a visitor, I want to search events by name so I can find a workshop faster.
- **Acceptance criteria:**
  1. The visitor can enter a word in a search field.
  2. The list shows events with that word in the name.
  3. If no event matches, the page shows "No events found".

## US-10 - Filter by date
- **Related feature:** F10 (Planned)
- **Role:** Visitor
- **User story:** As a visitor, I want to filter events by date so I can find an event on a suitable day.
- **Acceptance criteria:**
  1. The visitor can select a date.
  2. The list shows only events on that date.
  3. The visitor can clear the filter to see all upcoming public events.

## US-11 - Count registrations
- **Related feature:** F11 (Planned)
- **Role:** Organizer
- **User story:** As an organizer, I want to see the number of registrations for my events so I can check how many people will attend.
- **Acceptance criteria:**
  1. The organizer can see the number of active registrations for each own event.
  2. Cancelled registrations are not counted.
  3. The number is updated after a successful registration or cancellation.

## US-12 - Manage organizer accounts
- **Related feature:** F12 (Planned)
- **Role:** Admin
- **User story:** As an admin, I want to create and disable organizer accounts so I can control who can create events.
- **Acceptance criteria:**
  1. The admin can create an organizer account with an email address.
  2. The admin can disable an organizer account.
  3. A disabled organizer cannot log in.
