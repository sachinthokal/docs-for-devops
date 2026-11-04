# Helm Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **Helm**. This guide covers Kubernetes package management, Helm charts, Templating engine, Chart repositories, and release management.

---

## 📑 Table of Contents
1. [What is Helm?](#what-is-helm)
2. [Why Use Helm?](#why-use-helm)
3. [Core Concepts & Terminology](#core-concepts-terminology)
4. [Structure of a Helm Chart](#structure-of-a-helm-chart)
5. [Module Directory](#module-directory)

---

## What is Helm?

**Helm** is the official package manager for **Kubernetes** (often called the `apt` or `yum` of Kubernetes).

> **Key Definition**: Helm allows developers and operators to define, install, upgrade, and version complex Kubernetes applications through reusable packages called **Helm Charts**.

---

## Why Use Helm?

- **Simplifies Complex Apps**: Deploy multi-resource Kubernetes manifests (Deployments, Services, ConfigMaps, Ingress) in a single command.
- **Parameterization & Customization**: Customize deployments per environment (Dev, Staging, Prod) via `values.yaml` without modifying core YAML files.
- **Easy Upgrades & Rollbacks**: Atomic upgrades and one-command rollbacks (`helm rollback`).

---

## Core Concepts & Terminology

- **Helm Chart**: A package containing all resource definitions needed to run an application on Kubernetes.
- **Values (`values.yaml`)**: Configuration file containing variable values injected into chart templates.
- **Release**: A running instance of a Helm Chart deployed onto a Kubernetes cluster.
- **Chart Repository**: A HTTP server that hosts and distributes packaged charts (e.g., Artifact Hub).

---

## Structure of a Helm Chart

```
mychart/
├── Chart.yaml          # Metadata about the chart (version, description)
├── values.yaml         # Default configuration values for templates
├── templates/          # Directory of Go template files
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # Reusable template helper functions
└── charts/             # Sub-charts / dependencies
```

---

## Module Directory

- 🏛️ **[Helm Architecture](architecture.md)** — Helm v3 architecture, Go templating engine, Release tracking in Secrets.
- ⚙️ **[Helm Installations](installation.md)** — Installing Helm CLI on Linux, Windows, and macOS.
- ⚡ **[Helm Commands & Syntax](commands.md)** — Complete command reference for installing, upgrading, custom values, and chart creation.