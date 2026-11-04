# GitHub Commands & CLI Reference (`gh`) ⚡

A complete guide to using the official GitHub CLI (`gh`), Git remote integration commands, and GitHub API features directly from your terminal.

---

## 🎯 Quick Navigation
- [1. GitHub CLI Authentication & Config](#1-github-cli-authentication-config)
- [2. Managing Repositories](#2-managing-repositories)
- [3. Managing Pull Requests](#3-managing-pull-requests-prs)
- [4. Managing Issues](#4-managing-issues)
- [5. GitHub Actions Workflow Execution](#5-github-actions-workflow-execution)
- [6. Managing Gists, Releases & API](#6-managing-gists-releases-api)

---

## 1. GitHub CLI Authentication & Config

| Command | Description | Example |
| :--- | :--- | :--- |
| `gh auth login` | Start interactive login process. | `gh auth login` |
| `gh auth status` | Check authentication state. | `gh auth status` |
| `gh auth logout` | Log out from GitHub account. | `gh auth logout` |
| `gh config set` | Set GitHub CLI configuration defaults. | `gh config set editor "code --wait"` |

---

## 2. Managing Repositories

```bash
# Create a new repository on GitHub and local machine simultaneously
gh repo create my-new-app --public --clone

# Clone a GitHub repository
gh repo clone owner/repository

# Fork a repository to your account and clone locally
gh repo fork owner/repository --clone

# View repository details in browser or terminal
gh repo view
gh repo view --web

# List repositories belonging to user or organization
gh repo list owner
```

---

## 3. Managing Pull Requests (PRs)

```bash
# Create a Pull Request interactively
gh pr create --title "feat: user authentication" --body "Adds JWT login endpoint"

# List open Pull Requests for the current repository
gh pr list

# Checkout a Pull Request locally for testing
gh pr checkout 42

# View details and status of a Pull Request
gh pr view 42

# Review a Pull Request (Approve, Comment, or Request Changes)
gh pr review 42 --approve
gh pr review 42 --comment -b "Looks good!"

# Merge a Pull Request automatically
gh pr merge 42 --squash --delete-branch
```

---

## 4. Managing Issues

```bash
# Create a new issue
gh issue create --title "Bug: Login fails on Safari" --body "Detailed steps..."

# List issues in repository
gh issue list

# View issue details
gh issue view 12

# Assign an issue to a teammate
gh issue edit 12 --add-assignee "octocat"

# Close an issue
gh issue close 12
```

---

## 5. GitHub Actions Workflow Execution

```bash
# List all workflows in repository
gh run list

# View live log output of a specific run
gh run view <run_id> --log

# Trigger a manual workflow run (workflow_dispatch event)
gh workflow run deploy.yml

# Enable or disable a workflow
gh workflow enable deploy.yml
```

---

## 6. Managing Gists, Releases & API

### Gists
```bash
# Create a public or secret Gist from a file
gh gist create script.sh --public
gh gist create secret_config.json --secret
```

### Releases
```bash
# Create a release with tagged binaries
gh release create v1.0.0 ./dist/app.zip --title "v1.0.0 Release" --notes "First production release"
```

### Direct GitHub API Requests
```bash
# Send an authenticated GET request to GitHub REST API
gh api user

# Send a POST request to update repository topics
gh api repos/{owner}/{repo}/topics -X PUT -F "names[]=react" -F "names[]=typescript"
```