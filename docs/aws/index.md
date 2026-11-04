# Amazon Web Services (AWS) Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **Amazon Web Services (AWS)**. This guide covers core cloud infrastructure, global network, IAM security, EC2, S3, VPC networking, and AWS CLI management.

---

## 📑 Table of Contents
1. [What is Amazon Web Services (AWS)?](#what-is-amazon-web-services-aws)
2. [The AWS Shared Responsibility Model](#the-aws-shared-responsibility-model)
3. [Key Advantages of AWS](#key-advantages-of-aws)
4. [Core Concepts & Terminology](#core-concepts-terminology)
5. [Module Directory](#module-directory)

---

## What is Amazon Web Services (AWS)?

**Amazon Web Services (AWS)** is the world's most comprehensive and broadly adopted public cloud platform, offering over 200 fully featured services from datacenters globally.

> **Key Definition**: AWS provides on-demand cloud computing resources (servers, storage, databases, networking) on a pay-as-you-go pricing model without upfront hardware investments.

---

## The AWS Shared Responsibility Model

```
+-----------------------------------------------------------------------------------+
|                      CUSTOMER RESPONSIBILITY ("Security IN the Cloud")            |
|  - Customer Data, Identity & Access Management (IAM), OS Configuration & Patches  |
|  - Network Firewall Configuration (Security Groups / NACLs), Data Encryption     |
+-----------------------------------------------------------------------------------+
|                        AWS RESPONSIBILITY ("Security OF the Cloud")               |
|  - Physical Datacenters, Host Hardware, Hypervisors, Physical Networking         |
|  - Global Infrastructure (Regions, Availability Zones, Edge Locations)            |
+-----------------------------------------------------------------------------------+
```

---

## Key Advantages of AWS

- **Market Leader**: Broadest ecosystem of services, tools, and third-party integrations.
- **Pay-As-You-Go**: Scalable pricing without long-term contracts.
- **High Elasticity**: Auto Scaling capabilities to adjust capacity automatically based on demand.
- **Global Reach**: Dozens of AWS Regions and hundreds of CloudFront Edge Locations worldwide.

---

## Core Concepts & Terminology

- **AWS Region**: A physical geographic location containing multiple isolated, physically separate Availability Zones.
- **Availability Zone (AZ)**: One or more discrete datacenters with redundant power, networking, and connectivity.
- **IAM (Identity and Access Management)**: Controls authentication (who can log in) and authorization (what permissions they have).
- **EC2 (Elastic Compute Cloud)**: Scalable virtual servers in the cloud.
- **S3 (Simple Storage Service)**: Object storage service offering industry-leading scalability and durability.
- **VPC (Virtual Private Cloud)**: Logically isolated virtual network for your AWS resources.

---

## Module Directory

- 🏛️ **[AWS Architecture](architecture.md)** — IAM policy evaluation engine, VPC networking layout, S3 storage tiers, and AWS Global Infrastructure.
- ⚙️ **[AWS Installations](installation.md)** — Installing AWS CLI v2 and configuring credentials/profiles.
- ⚡ **[AWS Commands & CloudFormation Reference](commands.md)** — AWS CLI cheat sheet for EC2, S3, IAM, VPC, and CloudFormation syntax.