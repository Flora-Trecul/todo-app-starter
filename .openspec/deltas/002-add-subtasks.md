# Delta: Add Subtasks Feature

## Summary
Add Subtask model with one-to-many relationship to Todo, CRUD endpoints, and frontend integration.

## Changes

### Backend (api/)
- **models.py**: Added Subtask model with todo_id (FK), title, completed, position fields
- **models.py**: Added relationship between Todo and Subtask (bidirectional)
- **schemas.py**: Added SubtaskBase, SubtaskCreate, SubtaskUpdate, SubtaskResponse schemas
- **crud.py**: Added CRUD functions for Subtask (get_subtasks, get_subtask, create_subtask, update_subtask, delete_subtask)
- **main.py**: Added endpoints: GET /todos/{todo_id}/subtasks, POST /todos/{todo_id}/subtasks, PUT /todos/{todo_id}/subtasks/{subtask_id}, DELETE /todos/{todo_id}/subtasks/{subtask_id}

### Frontend (web/)
- **types.ts**: Added Subtask, SubtaskCreate, SubtaskUpdate interfaces
- **types.ts**: Added subtasks field to Todo interface
- **api.ts**: Added listSubtasks, createSubtask, updateSubtask, deleteSubtask methods
- **TodoItem.svelte**: Added subtask list display with checkboxes
- **TodoItem.svelte**: Added form to create new subtasks
- **TodoItem.svelte**: Added expand/collapse functionality
- **+page.svelte**: Added subtask loading and handlers

## Test Results
- [x] GET /todos/{todo_id}/subtasks returns subtasks for a todo
- [x] POST /todos/{todo_id}/subtasks creates a subtask
- [x] PUT /todos/{todo_id}/subtasks/{subtask_id} updates a subtask
- [x] DELETE /todos/{todo_id}/subtasks/{subtask_id} deletes a subtask
- [x] Frontend displays subtasks under parent todo
- [x] Frontend allows adding subtasks
- [x] Cascade delete works when todo is deleted

## Status
✅ Implemented and tested
