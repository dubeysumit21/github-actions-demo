# github-actions-demo

A demo Python project showcasing GitHub Actions CI pipeline with live log streaming via curl.

## Structure

```
src/        - Application source
tests/      - Test suite
.github/    - GitHub Actions workflows
```

## Workflow Jobs

| Job      | Purpose                        |
|----------|-------------------------------|
| lint     | Code style and formatting     |
| build    | Dependency and import checks  |
| test     | Unit tests and coverage       |
| security | Static security scanning      |
| deploy   | Artifact packaging            |
