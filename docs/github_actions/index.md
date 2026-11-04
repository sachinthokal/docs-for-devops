# GitHub Actions Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **GitHub Actions**. This guide covers native CI/CD workflows on GitHub, runner execution models, workflow syntax, triggers, custom actions, and production management.

---

## 📑 Table of Contents
1. [What is GitHub Actions?](#what-is-github-actions)
2. [Key Concepts & Terminology](#key-concepts-terminology)
3. [Benefits of GitHub Actions](#benefits-of-github-actions)
4. [Standard Workflow File Structure](#standard-workflow-file-structure)
5. [Module Directory](#module-directory)

---

## What is GitHub Actions?

**GitHub Actions** is a native Continuous Integration and Continuous Deployment (CI/CD) platform integrated directly into GitHub repositories. It allows you to automate your build, test, and deployment pipelines through YAML configuration files.

> **Key Definition**: GitHub Actions enables event-driven automation directly inside your repository—triggering workflows on code pushes, pull requests, issue creations, or scheduled cron jobs.

---

## Key Concepts & Terminology

- **Workflow**: An automated, configurable process defined in a `.github/workflows/*.yml` file.
- **Event**: A specific activity that triggers a workflow (e.g., `push`, `pull_request`, `schedule`).
- **Job**: A set of steps executed on the same runner/virtual machine. Jobs run in parallel by default.
- **Step**: An individual task inside a job. A step can execute shell commands or run an Action.
- **Action**: A reusable, standalone application or script that performs a complex task (e.g., `actions/checkout`).
- **Runner**: A server that executes jobs when a workflow is triggered (GitHub-hosted or Self-hosted).

---

## Benefits of GitHub Actions

- **Native Integration**: No external CI/CD setup required; managed directly inside GitHub.
- **Rich Marketplace**: Access thousands of pre-built reusable actions in the GitHub Marketplace.
- **Matrix Builds**: Run tests across multiple OS versions and runtime environments simultaneously.
- **Secret Management**: Built-in encrypted repository and environment secrets.

---

## Standard Workflow File Structure

```yaml
name: CI Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Build Script
        run: echo "Building application..."
```

---

## Module Directory

- 🏛️ **[GitHub Actions Architecture](architecture.md)** — Event dispatchers, Hosted vs Self-hosted runners, Action types, and Matrix strategies.
- ⚙️ **[GitHub Actions Installations](installation.md)** — Setting up self-hosted runners on Linux, Windows, and macOS servers.
- ⚡ **[GitHub Actions Commands & Syntax](commands.md)** — Complete YAML syntax cheat sheet, expression evaluation, and GitHub CLI workflow triggers.