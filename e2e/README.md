# Playwright E2E Tests

This directory contains end-to-end tests for the To-Do application using [Playwright](https://playwright.dev/).

## Setup

Playwright is already installed as a dev dependency:

```bash
# Install browsers (run once)
bun add -D @playwright/mcp playwright
# Browsers are automatically installed with the package
```

## Running Tests

### Basic Test Execution

```bash
# Run all tests
bun run test:e2e

# Run tests with UI mode (great for debugging)
bun run test:e2e:ui

# Run tests with browser visible
bun run test:e2e:headed

# Run tests with debug mode
bun run test:e2e:debug
```

### Specific Test Files

```bash
# Run a specific test file
bunx playwright test e2e/specs/main.spec.ts

# Run a specific test
bunx playwright test e2e/specs/main.spec.ts -g "should add a new task"
```

## MCP Server

This project uses [@playwright/mcp](https://github.com/playwright/mcp) to enable AI agents to interact with Playwright.

### Starting the MCP Server

```bash
# Start the MCP server for AI agent integration
bun run playwright:mcp
```

The MCP server provides AI agents with the ability to:
- Execute Playwright tests
- Run browser automation
- Capture screenshots and videos
- Generate test reports

### MCP Configuration

The MCP server can be configured with environment variables:

```bash
# Set base URL for tests
PLAYWRIGHT_BASE_URL=http://localhost:8080

# Enable headless mode
HEADLESS=true
```

## Configuration

The main configuration file is `playwright.config.ts`:

- **Test directory**: `./e2e`
- **Base URL**: `http://localhost:8080` (configurable via `PLAYWRIGHT_BASE_URL`)
- **Browsers**: Chromium, Firefox, WebKit
- **Reporter**: HTML (generates `playwright-report/index.html`)
- **Web server**: Automatically starts Docker Compose in development mode

## Writing Tests

Tests are written using the [Playwright Test API](https://playwright.dev/docs/test-api):

```typescript
import { test, expect } from '@playwright/test';

test('example test', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/To-Do/);
});
```

### Best Practices

1. **Use `test.describe`** to group related tests
2. **Use `test.beforeEach`** for common setup
3. **Use `expect`** for assertions
4. **Use selectors** like `getByRole()`, `getByText()`, `getByPlaceholder()`
5. **Avoid hardcoded timeouts** - use Playwright's auto-waiting

## CI/CD Integration

To run tests in CI/CD:

```yaml
# .github/workflows/test.yml
name: E2E Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: oven-sh/setup-bun@v2
      - run: bun install
      - run: bunx playwright install chromium
      - run: bunx playwright test
        env:
          PLAYWRIGHT_BASE_URL: http://localhost:8080
          CI: true
```

## Test Reports

After running tests, Playwright generates:
- **HTML Report**: `playwright-report/index.html`
- **JSON Report**: `test-results/`
- **Traces**: `test-results/` (when enabled)
- **Screenshots**: `test-results/` (on failure)
- **Videos**: `test-results/` (on failure)

## Troubleshooting

### Docker Server Not Starting

If you're running tests locally without Docker:

```bash
# Start the server manually first
docker compose up --build -d

# Then run tests with existing server
bunx playwright test --port 8080
```

### Browser Not Installed

```bash
# Install specific browser
bunx playwright install chromium
bunx playwright install firefox
bunx playwright install webkit

# Install all browsers
bunx playwright install
```

### Tests Failing in CI

- Make sure Docker Compose can start (check ports, volumes)
- Set `CI=true` environment variable
- Use `--retries` for flaky tests
