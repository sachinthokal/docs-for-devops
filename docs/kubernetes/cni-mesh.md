# Kubernetes Networking, CNI & Service Mesh

A comprehensive guide to Kubernetes Pod networking, Container Network Interface (CNI) plugins, and Service Mesh architecture.

---

## The Kubernetes Network Model

Kubernetes enforces three fundamental networking requirements:

1. All pods can communicate with all other pods on any node without NAT.
2. Agents on a node (e.g. `kubelet`) can communicate with all pods on that same node.
3. Containers within a pod share their network namespace (IP address and port space via `localhost`).

---

## Container Network Interface (CNI)

CNI defines a standardized plugin-based interface for configuring network interfaces for Linux containers.

| CNI Plugin | Primary Features | Network Mode |
| :--- | :--- | :--- |
| **Calico** | Rich network security policies, BGP routing, eBPF data plane support | Overlay (VXLAN/IPIP) or Flat L3 (BGP) |
| **Cilium** | High-performance networking, eBPF-native packet routing, transparent encryption | eBPF Kernel Routing |
| **Flannel** | Minimal configuration, simple overlay networking | VXLAN / host-gw |
| **AWS VPC CNI** | Direct allocation of AWS ENI IP addresses to Pods | Native VPC routing |

---

## NetworkPolicies

NetworkPolicies act as packet-filtering firewalls for pods using label selectors:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-ingress-restriction
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: backend-api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

---

## Service Mesh Overview

A Service Mesh (e.g., **Istio**, **Linkerd**) adds an infrastructure layer for microservice communication, providing:

- Mutual TLS (mTLS) traffic encryption.
- Advanced traffic shaping (canary, blue-green, fault injection).
- Distributed tracing and metrics telemetry without modifying application code.

