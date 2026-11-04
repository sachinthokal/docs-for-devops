# DevSecOps Complete Guide: Zero to Hero 🚀

Welcome to the ultimate guide on **DevSecOps**. This guide covers shifting security left, security testing types (SAST, DAST, SCA, IAST), secret scanning, container security, and CI/CD security integration.

---

## 📑 Table of Contents
1. [What is DevSecOps?](#what-is-devsecops)
2. [Shift Left Security Principle](#shift-left-security-principle)
3. [Key Security Testing Methodologies](#key-security-testing-methodologies)
4. [Key Benefits of DevSecOps](#key-benefits-of-devsecops)
5. [Module Directory](#module-directory)

---

## What is DevSecOps?

**DevSecOps** (Development, Security, and Operations) is the practice of integrating security testing and compliance checks seamlessly into every phase of the software development lifecycle (SDLC), rather than treating security as an isolated, final audit step.

> **Key Definition**: DevSecOps automates security controls within the CI/CD pipeline, ensuring that code, third-party dependencies, container images, and cloud infrastructure are scanned for vulnerabilities before reaching production.

---

## Shift Left Security Principle

```
TRADITIONAL DEVOPS (Security as a bottleneck at the end)
[ Plan ] -> [ Code ] -> [ Build ] -> [ Test ] -> [ Deploy ] -> | SECURITY AUDIT | -> Outage/Fixes

DEVSECOPS (Shift-Left Security embedded continuously)
[ Plan ]  ->  [ Code ]  ->  [ Build ]  ->  [ Test ]  ->  [ Deploy ]
  (Threat       (SAST &       (SCA &        (DAST &       (Runtime &
  Modeling)    Linting)      Container)    PenTest)       Guardrails)
```

---

## Key Security Testing Methodologies

| Security Type | Full Name | Focus Area | Example Tools |
| :--- | :--- | :--- | :--- |
| **SAST** | Static Application Security Testing | Source code static analysis for code flaws. | SonarQube, Semgrep, Checkmarx |
| **SCA** | Software Composition Analysis | Open-source dependencies & CVE scanning. | Trivy, Snyk, OWASP Dependency-Check |
| **Secret Scanning** | Hardcoded Credentials Detection | Scans git commit history for keys/passwords. | Trufflehog, Gitleaks |
| **Container Sec** | Container Image Vulnerability Scanning| Scans OS packages inside Docker images. | Trivy, Grype, Clair |
| **DAST** | Dynamic Application Security Testing | Web vulnerability scanning against running apps.| OWASP ZAP, Burp Suite |

---

---

## Key Benefits of DevSecOps

- **Proactive Vulnerability Discovery**: Identifies security vulnerabilities early in development when they are least costly and fastest to fix.
- **Automated Compliance**: Enforces regulatory and security policies automatically in continuous integration pipelines.
- **Accelerated Time to Market**: Reduces release delays caused by last-minute manual security audits.
- **Shared Responsibility Culture**: Unifies developers, operations, and security teams with transparent security metrics.

## Module Directory

- 🏛️ **[DevSecOps Architecture](architecture.md)** — Security gates in CI/CD, Threat modeling, SBOM generation, and Policy as Code.
- ⚙️ **[DevSecOps Installations](installation.md)** — Setting up SonarQube, Trivy, and Gitleaks in local and CI/CD pipelines.
- ⚡ **[DevSecOps Commands & Pipeline Examples](commands.md)** — Complete command reference for Trivy, Gitleaks, SonarQube CLI, and DevSecOps GitHub Actions pipeline.