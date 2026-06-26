# Testing Skill

**Name:** testing

**Description:** Run end-to-end tests using Playwright to validate application functionality

**When to use:** When you need to verify that the application works correctly end-to-end

## Commands

### Run all E2E tests
```bash
bun run test:e2e
```

### Run tests with UI mode
```bash
bun run test:e2e:ui
```

### Run tests with visible browser
```bash
bun run test:e2e:headed
```

### Run specific test file
```bash
bunx playwright test e2e/specs/main.spec.ts
```

### Start MCP server for AI agent integration
```bash
bun run playwright:mcp
```

## Configuration

Playwright is configured in `playwright.config.ts`:
- Base URL: `http://localhost:8080`
- Browsers: Chromium, Firefox, WebKit
- Timeout: 30s for tests, 5s for assertions
- Reporter: HTML

## Test Files

Tests are located in `e2e/specs/`:
- `main.spec.ts` - Main page functionality tests

## MCP Integration

The Playwright MCP server allows AI agents to:
- Execute Playwright tests programmatically
- Run browser automation
- Capture screenshots and videos
- Generate test reports

## Before Running Tests

1. Ensure Docker Compose services are running:
   ```bash
   docker compose up --build -d
   ```

2. Or start services manually:
   ```bash
   cd api && uv run uvicorn main:app --reload --port 8000
   cd web && bun run dev
   ```

## CI/CD

For GitHub Actions, see `e2e/README.md` for complete CI/CD integration guide.
