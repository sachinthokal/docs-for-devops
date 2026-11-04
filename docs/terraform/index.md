# Terraform Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **Terraform**. This guide covers Infrastructure as Code (IaC) principles, declarative resource provisioning, HCL syntax, state management, and enterprise workflows.

---

## 📑 Table of Contents
1. [What is Terraform & IaC?](#what-is-terraform-iac)
2. [Imperative vs. Declarative IaC](#imperative-vs-declarative-iac)
3. [Key Benefits of Terraform](#key-benefits-of-terraform)
4. [Core Concepts & Terminology](#core-concepts-terminology)
5. [The Standard Terraform Workflow](#the-standard-terraform-workflow)
6. [Module Directory](#module-directory)

---

## What is Terraform & IaC?

### What is Infrastructure as Code (IaC)?
**Infrastructure as Code (IaC)** is the practice of managing and provisioning computing infrastructure (servers, networks, databases, firewalls) through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

### What is Terraform?
**Terraform** is an open-source Infrastructure as Code tool created by **HashiCorp**. It allows developers and DevOps engineers to define both cloud and on-premises resources in human-readable configuration files using **HCL (HashiCorp Configuration Language)**.

> **Key Definition**: Terraform provides a unified workflow to provision, change, and version-control infrastructure safely and efficiently across multiple cloud providers (AWS, Azure, GCP, Kubernetes) simultaneously.

---

## Imperative vs. Declarative IaC

| Feature | Imperative IaC (e.g., Bash, AWS CLI) | Declarative IaC (Terraform) |
| :--- | :--- | :--- |
| **Approach** | You define **how** to achieve the state (step-by-step scripts). | You define **what** the final state should look like. |
| **State Tracking** | No built-in state awareness; risk of duplicate provisioning. | Maintains a `.tfstate` file to track real-world resources. |
| **Idempotency** | Difficult to guarantee without extra logic. | Built-in idempotency (re-applying produces exact target state). |

---

## Key Benefits of Terraform

- **Cloud-Agnostic**: Single workflow to manage multi-cloud infrastructure (AWS, GCP, Azure, OpenStack).
- **State Management**: Tracks real-world resource state and maps configurations to deployed infrastructure.
- **Dependency Graph**: Automatically determines resource dependencies and parallelizes provisioning.
- **Drift Detection**: Detects manual changes made outside of Terraform and restores desired state.

---

## Core Concepts & Terminology

- **HCL (HashiCorp Configuration Language)**: The declarative configuration language used by Terraform.
- **Provider**: A plugin that translates HCL definitions into API calls for specific platforms (e.g., AWS, Azure, GCP).
- **Resource**: An infrastructure object (VM, VPC, S3 bucket, Security Group) defined in code.
- **State File (`.tfstate`)**: A JSON file mapping configuration resources to real-world cloud IDs.
- **Module**: A container for multiple resources configured together to encourage reusability.

---

## The Standard Terraform Workflow

1. **Write**: Define infrastructure resources in `.tf` files using HCL.
2. **Init**: Run `terraform init` to download required provider plugins and modules.
3. **Plan**: Run `terraform plan` to preview execution plan and changes before applying.
4. **Apply**: Run `terraform apply` to provision or modify infrastructure to match target configuration.
5. **Destroy**: Run `terraform destroy` to tear down managed infrastructure safely.

---

## Module Directory

- 🏛️ **[Terraform Architecture](architecture.md)** — Core vs Plugins, Provider registry, Dependency graphs, State locking, and Remote Backends.
- ⚙️ **[Terraform Installations](installation.md)** — Installing Terraform CLI on Linux, Windows, and macOS, plus tfenv setup.
- ⚡ **[Terraform Commands](commands.md)** — Complete command reference, CLI flags, workspace management, and HCL code templates.