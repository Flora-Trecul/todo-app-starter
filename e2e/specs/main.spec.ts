import { test, expect } from '@playwright/test';

test.describe('To-Do App Main Page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should display main heading', async ({ page }) => {
    await expect(page.getByRole('heading', { name: 'To-Do' })).toBeVisible();
  });

  test('should display add task form', async ({ page }) => {
    await expect(page.getByPlaceholder('What needs to be done?')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Add task' })).toBeVisible();
  });

  test('should add a new task', async ({ page }) => {
    const taskTitle = 'Test E2E Task';
    
    await page.getByPlaceholder('What needs to be done?').fill(taskTitle);
    await page.getByRole('button', { name: 'Add task' }).click();
    
    await expect(page.getByText(taskTitle)).toBeVisible();
  });

  test('should toggle task completion', async ({ page }) => {
    const taskTitle = 'Toggle Test Task';
    
    // Create a task
    await page.getByPlaceholder('What needs to be done?').fill(taskTitle);
    await page.getByRole('button', { name: 'Add task' }).click();
    
    // Find the task checkbox and toggle it
    const taskCheckbox = page.getByRole('checkbox', { name: new RegExp(taskTitle) });
    await taskCheckbox.check();
    
    // Verify the task is marked as completed (has line-through)
    const taskText = page.getByText(taskTitle).first();
    await expect(taskText).toHaveClass(/line-through/);
    
    // Uncheck it
    await taskCheckbox.uncheck();
    
    // Verify the task is active again
    await expect(taskText).not.toHaveClass(/line-through/);
  });

  test('should display filter buttons', async ({ page }) => {
    await expect(page.getByRole('button', { name: 'all' })).toBeVisible();
    await expect(page.getByRole('button', { name: 'active' })).toBeVisible();
    await expect(page.getByRole('button', { name: 'completed' })).toBeVisible();
  });

  test('should display task counts', async ({ page }) => {
    await expect(page.getByText(/total/).first()).toBeVisible();
    await expect(page.getByText(/active/).first()).toBeVisible();
    await expect(page.getByText(/done/).first()).toBeVisible();
  });
});
