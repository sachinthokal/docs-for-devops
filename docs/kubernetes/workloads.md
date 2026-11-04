# Kubernetes Workloads Architecture

A structured breakdown of workload controllers, pod abstractions, and life-cycle management patterns in Kubernetes.

---

## Workload Controller Overview

Workload controllers manage collections of Pods to guarantee declared desired state, reconciliation, and automated self-healing.

| Controller | Purpose | Use Case |
| :--- | :--- | :--- |
| **Deployment** | Declarative updates for Pods & ReplicaSets | Stateless web apps, REST APIs, microservices |
| **StatefulSet** | Unique network identities and ordered, persistent storage | Databases, Kafka brokers, distributed datastores |
| **DaemonSet** | Ensures a copy of a Pod runs on all (or selected) nodes | Log forwarders (`fluentbit`), monitoring agents, CNI daemons |
| **Job** | Runs finite batch tasks to completion | Database migrations, batch ETL jobs |
| **CronJob** | Runs recurring scheduled batch jobs | Backups, cleanup routines, daily report generation |

---

## Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-api
  labels:
    app: web-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-api
  template:
    metadata:
      labels:
        app: web-api
    spec:
      containers:
        - name: web-api
          image: nginx:alpine
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "250m"
              memory: "256Mi"
```
