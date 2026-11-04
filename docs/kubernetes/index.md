# Kubernetes Documentation

Welcome to the Kubernetes documentation hub for this project. Use the navigation links below to explore cluster setups, core architecture, configuration guides, and operational commands.

---

## Kubernetes Contents

### 1. Architecture & Core Concepts

* [**Architecture Overview**](architecture.md) – Detailed breakdown of Control Plane, Worker Node, and OCI container basics.
* [**Kubernetes Workloads**](workloads.md) – Overview of Pods, Deployments, StatefulSets, DaemonSets, Jobs, and CronJobs.

### 2. Setup & Installation

* [**Kind Cluster Setup**](kind.md) – Step-by-step guide to setting up a local multi-node cluster using Kind.
* [**Minikube Cluster Setup**](minikube.md) – Local cluster setup, addons, and management with Minikube.

### 3. Storage & Configuration

* [**Volumes & Storage**](storage.md) – PersistentVolumes (PV), PersistentVolumeClaims (PVC), StorageClasses, and CSI drivers.
* [**ConfigMaps & Secrets**](config-secrets.md) – Application configs, opaque secrets, base64 encoding, and External Secrets Operator (ESO).

### 4. Networking & Service Mesh

* [**Services & Ingress**](services-ingress.md) – Routing traffic using ClusterIP, NodePort, LoadBalancer, and NGINX Ingress Controllers.
* [**CNI & Service Mesh**](cni-mesh.md) – Pod networking with Calico/Cilium, NetworkPolicies, and Istio mTLS basics.

### 5. Application Health & Autoscaling

* [**Health Probes**](probes.md) – Configuring Liveness, Readiness, and Startup probes.
* [**Resource Management & Scaling**](autoscaling.md) – Resource Requests/Limits, HPA, VPA, and Cluster Autoscaler / Karpenter.

### 6. Security & Access Control (RBAC)

* [**RBAC & Service Accounts**](rbac.md) – User and workload authentication via Roles, ClusterRoles, and RoleBindings.
* [**Pod & Network Security**](pod-security.md) – Enforcing Pod Security Admission (PSA), SecurityContext, and NetworkPolicies.

### 7. Package Management & GitOps

* [**Helm Package Manager**](../helm/index.md) – Building and deploying applications using Helm Charts and values files.
* [**GitOps Workflows**](../gitops/index.md) – Declarative continuous delivery with ArgoCD and FluxCD.

### 8. Observability & Logging

* [**Monitoring & Metrics**](../observability/index.md) – Scraping cluster metrics using Prometheus, Grafana, and Kube-State-Metrics.
* [**Logging & Tracing**](../observability/commands.md) – Aggregating pod logs using EFK and Grafana Loki.

### 9. Cluster Operations & Disaster Recovery

* [**Command Cheat Sheet**](commands.md) – Essential `kubectl` operational commands, context switching, and quick reference.
* [**Troubleshooting Guide**](commands.md#8-debugging-troubleshooting) – Resolving CrashLoopBackOff, ImagePullBackOff, Pending pods, and log inspection.

---

## Quick Start

1. Ensure `kubectl` and a local cluster engine (Minikube, Kind, or Docker Desktop) are installed and running.

> kubectl version

1. Clone the repository to your local machine:

   > git clone repository-url && cd repository-directory

2. Apply the Kubernetes manifests:

> kubectl apply -f ./manifests/

---
