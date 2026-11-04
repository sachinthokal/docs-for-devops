# Microsoft Azure Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **Microsoft Azure**. This guide covers core cloud concepts, resource hierarchy, compute, networking, storage, security, and Azure management tools.

---

## 📑 Table of Contents
1. [What is Microsoft Azure?](#what-is-microsoft-azure)
2. [Cloud Service Models (IaaS, PaaS, SaaS)](#cloud-service-models-iaas-paas-saas)
3. [Key Benefits of Azure](#key-benefits-of-azure)
4. [Core Concepts & Terminology](#core-concepts-terminology)
5. [Module Directory](#module-directory)

---

## What is Microsoft Azure?

**Microsoft Azure** is a leading global public cloud computing platform providing over 200 IaaS, PaaS, and SaaS services including virtual computing, storage, networking, analytics, databases, and DevOps.

> **Key Definition**: Azure allows organizations to build, deploy, manage, and scale applications across a vast global network of Microsoft-managed datacenters.

---

## Cloud Service Models (IaaS, PaaS, SaaS)

| Model | Description | Azure Example |
| :--- | :--- | :--- |
| **IaaS** | Infrastructure as a Service (VMs, Disks, VNets). You manage OS and apps. | Azure Virtual Machines (VMs) |
| **PaaS** | Platform as a Service. Azure manages OS/runtime; you focus on code. | Azure App Service, Azure SQL |
| **SaaS** | Software as a Service. Complete end-user software solution hosted in cloud. | Microsoft 365, Power BI |

---

## Key Benefits of Azure

- **Global Presence**: Available across 60+ regions worldwide with high-availability Availability Zones.
- **Hybrid Cloud**: Seamless hybrid integration using **Azure Arc** and **Azure ExpressRoute**.
- **Enterprise Security**: Native identity management via **Microsoft Entra ID** (formerly Azure AD).
- **Compliance**: Highest number of industry and government compliance certifications.

---

## Core Concepts & Terminology

- **Tenant**: A dedicated instance of Microsoft Entra ID representing an organization.
- **Subscription**: An agreement with Microsoft to use cloud services; serves as a billing and management boundary.
- **Resource Group**: A logical container that holds related Azure resources for a project or environment.
- **Resource**: An manageable item available through Azure (e.g., Virtual Machine, Storage Account, VNet).
- **ARM (Azure Resource Manager)**: The management layer used to create, update, and delete resources.

---

## Module Directory

- 🏛️ **[Azure Architecture](architecture.md)** — Subscriptions, Resource Groups, ARM template engine, Virtual Networks, and Regions/Zones.
- ⚙️ **[Azure Installations](installation.md)** — Installing Azure CLI (`az`), Azure PowerShell module, and Bicep compiler.
- ⚡ **[Azure Commands & Bicep Syntax](commands.md)** — Comprehensive Azure CLI (`az`) cheat sheet and sample Bicep infrastructure template.