# Delta: Add Reminders Feature

## Summary
Add reminder_date field to Todo model and API endpoints to support task reminders.

## Changes

### Backend (api/)
- **models.py**: Added `reminder_date = Column(DateTime(timezone=True), nullable=True)` to Todo model
- **schemas.py**: Added `reminder_date: datetime | None = Field(default=None)` to TodoBase, TodoUpdate
- **crud.py**: Added `get_todos_with_upcoming_reminders(db, now)` function
- **main.py**: Added `GET /reminders` endpoint

### Frontend (web/)
- **types.ts**: Added `reminder_date: string | null | undefined` to Todo, TodoCreate, TodoUpdate interfaces
- **api.ts**: Added `listUpcomingReminders: () => request<Todo[]>('/reminders')` method
- **TodoItem.svelte**: Added bell icon indicator when reminder_date is set

## Test Results
- [x] POST /todos with reminder_date creates todo with reminder
- [x] GET /todos returns todos with reminder_date
- [x] GET /reminders returns only todos with future reminder_date
- [x] Frontend displays reminder icon on todos with reminders

## Status
✅ Implemented and tested
