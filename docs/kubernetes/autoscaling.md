# Kubernetes Autoscaling & Resource Management

A reference guide for managing resources, requests, limits, and autoscaling workloads in Kubernetes clusters.

---

## Overview

Kubernetes offers multiple dimensions of autoscaling:

1. **Horizontal Pod Autoscaler (HPA)**: Scales the number of pod replicas based on observed CPU/memory utilization or custom metrics.
2. **Vertical Pod Autoscaler (VPA)**: Automatically adjusts CPU and memory reservations for pods based on historical resource usage.
3. **Cluster Autoscaler & Karpenter**: Dynamically scales the underlying worker nodes up or down according to pending pod resource demands.

---

## Resource Requests and Limits

Every container within a pod can specify resource requests and limits:

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

- **Requests**: Guaranteed baseline resources required to schedule the pod onto a node.
- **Limits**: Hard ceiling; containers exceeding memory limits trigger OOMKills (`OOMKilled`).

---

## Horizontal Pod Autoscaler (HPA) Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 75
```

---

## Related Guides

- [Kubernetes Architecture](architecture.md)
- [Kubernetes Commands Cheat Sheet](commands.md)
- [Health Probes](probes.md)

