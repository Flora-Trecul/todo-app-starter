export interface Subtask {
	id: number;
	todo_id: number;
	title: string;
	completed: boolean;
	position: number;
}

export interface SubtaskCreate {
	title: string;
	completed?: boolean;
	position?: number;
}

export interface SubtaskUpdate {
	title?: string;
	completed?: boolean;
	position?: number;
}

export interface Todo {
	id: number;
	title: string;
	description: string | null;
	completed: boolean;
	reminder_date: string | null | undefined;
	created_at: string;
	updated_at: string | null;
	subtasks?: Subtask[] | undefined;
}

export interface TodoCreate {
	title: string;
	description?: string | null;
	completed?: boolean;
	reminder_date?: string | null;
}

export interface TodoUpdate {
	title?: string;
	description?: string | null;
	completed?: boolean;
	reminder_date?: string | null;
}

export type Filter = 'all' | 'active' | 'completed';
