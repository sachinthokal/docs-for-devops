# Azure DevOps Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **Azure DevOps (ADO)**. This guide covers Azure Pipelines, Repos, Boards, Artifacts, YAML pipelines, agent pools, and enterprise CI/CD integration.

---

## 📑 Table of Contents
1. [What is Azure DevOps?](#what-is-azure-devops)
2. [Core Services of Azure DevOps](#core-services-of-azure-devops)
3. [Key Concepts & Terminology](#key-concepts-terminology)
4. [Classic Editor vs YAML Pipelines](#classic-editor-vs-yaml-pipelines)
5. [Module Directory](#module-directory)

---

## What is Azure DevOps?

**Azure DevOps** is an enterprise-grade SaaS and on-premises suite provided by Microsoft that provides end-to-end DevOps toolchains for developing, testing, building, and deploying applications.

> **Key Definition**: Azure DevOps combines Agile planning tools (Boards), code hosting (Repos), enterprise CI/CD pipelines (Pipelines), package hosting (Artifacts), and automated testing (Test Plans).

---

## Core Services of Azure DevOps

| Service | Function |
| :--- | :--- |
| **Azure Boards** | Agile project management, Kanban boards, backlogs, and task tracking. |
| **Azure Repos** | Git repository hosting and Team Foundation Version Control (TFVC). |
| **Azure Pipelines** | Language, platform, and cloud-agnostic CI/CD engine. |
| **Azure Artifacts** | Hosted package management (npm, NuGet, Maven, Python, Universal Packages). |
| **Azure Test Plans** | Manual and exploratory testing framework. |

---

## Key Concepts & Terminology

- **Organization**: The top-level boundary in Azure DevOps hosting projects.
- **Project**: A isolated container inside an organization holding boards, repos, pipelines, and artifacts.
- **Pipeline**: The workflow configuration that defines how code is built, tested, and deployed.
- **Stage**: A logical collection of related jobs (e.g., `Build`, `Test`, `Deploy_Staging`, `Deploy_Prod`).
- **Job**: A series of steps run by an agent node.
- **Agent Pool**: A cluster of build/deployment agents (Microsoft-hosted or Self-hosted).
- **Service Connection**: Secure credential configuration enabling Pipelines to connect to external clouds (Azure, AWS, Kubernetes).

---

## Classic Editor vs YAML Pipelines

| Feature | Classic Editor | YAML Pipelines (Recommended) |
| :--- | :--- | :--- |
| **Configuration** | GUI-driven point-and-click | Version-controlled `azure-pipelines.yml` code |
| **Version Control** | Separate from source code | Tracked and reviewed in Git Pull Requests |
| **Reusability** | Task groups | Reusable templates and composite steps |
| **Disaster Recovery** | Manual recreation or export | Instantly restored from repository history |

---

## Module Directory

- 🏛️ **[Azure DevOps Architecture](architecture.md)** — Agent pools, Service connections, Variable groups, and Multi-stage DAG pipelines.
- ⚙️ **[Azure DevOps Installations](installation.md)** — Setting up Azure DevOps Self-Hosted Build Agents on Linux and Windows.
- ⚡ **[Azure DevOps Commands & Syntax](commands.md)** — Azure Pipeline YAML syntax, templates, condition expressions, and Azure CLI (`az devops`) commands.