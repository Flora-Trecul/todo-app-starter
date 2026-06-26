# Subtasks Feature - Requirements

## User Story
As a user, I want to break down my tasks into subtasks so I can better organize and track my work.

## Acceptance Criteria
- [ ] Subtask model with fields: id, todo_id, title, completed, position
- [ ] CRUD endpoints for subtasks: GET /todos/{todo_id}/subtasks, POST, PUT, DELETE
- [ ] Cascade delete: deleting a todo deletes its subtasks
- [ ] Frontend displays subtasks list under parent todo
- [ ] Frontend allows adding new subtasks
- [ ] Frontend allows toggling subtask completion
- [ ] Frontend allows deleting subtasks

## Out of Scope
- Drag-and-drop reordering (future enhancement)
- Nested subtasks (future enhancement)
- Subtask reminders (future enhancement)
