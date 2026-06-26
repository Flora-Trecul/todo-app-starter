export interface Todo {
	id: number;
	title: string;
	description: string | null;
	completed: boolean;
	reminder_date: string | null | undefined;
	created_at: string;
	updated_at: string | null;
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
