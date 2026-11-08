
# ADR 0002 - Database

** Status
Accepted

** Context
We need to store events, users and registrations.

** Alternatives
- PostgreSQL
- SQLite

** Decision
We choose PostgreSQL because it supports relational data.

** Consequences
- Positive: PostgreSQL supports connected tables.
- Negative: It needs separate installation and setup.
