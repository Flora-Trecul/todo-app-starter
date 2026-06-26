# Reminders Feature - Requirements

## User Story
As a user, I want to set reminders on important tasks so I don't forget them.

## Acceptance Criteria
- [ ] Todo model has optional `reminder_date` field (nullable DateTime)
- [ ] Todo can be created/updated with reminder_date via API
- [ ] GET /todos returns todos with reminder_date
- [ ] GET /todos/upcoming-reminders returns todos with future reminder_date
- [ ] Frontend displays reminder indicator on todos with reminders

## Out of Scope
- Email notifications (future enhancement)
- Web push notifications (future enhancement)
- Recurring reminders (future enhancement)
