---
name: frontend
description: SvelteKit frontend development with Tailwind CSS v4 and TypeScript. Follows Svelte 5 runes and project conventions.
user-invocable: true
---

# Frontend Development Guidelines

## Tech Stack
- Framework: SvelteKit 2
- Svelte: 5 runes
- Styling: Tailwind CSS v4
- Language: TypeScript
- Bundler: Vite

## Structure
- Routes: `web/src/routes/`
- Components: `web/src/lib/components/`
- API client: `web/src/lib/api.ts`

## Conventions
- PascalCase for Svelte components
- camelCase for variables/functions
- Use $state, $derived, $props runes (no legacy $: syntax)
- Utility classes inline for Tailwind

## Testing
- Use vitest for component tests
- Test files: `web/tests/*.test.ts`

## Commands
- Dev server: `cd web && bun run dev`
- Type check: `cd web && bun run check`
- Tests: `cd web && bun run test`
