# Kubernetes Services & Ingress Networking

Exposing containerized workloads inside and outside the Kubernetes cluster using Services and Ingress Controllers.

---

## Service Types

Kubernetes Services provide stable networking abstraction and round-robin load balancing across dynamic sets of ephemeral pods:

| Type | Target Scope | Use Case |
| :--- | :--- | :--- |
| **ClusterIP** | Internal cluster only | Default service type for internal microservice communication |
| **NodePort** | Static port on each Node (30000-32767) | Direct external node access for testing/debugging |
| **LoadBalancer** | Cloud provider load balancer (NLB/ALB) | Public-facing production workloads |
| **ExternalName** | CNAME DNS record redirect | Alias an internal service to an external hostname |

---

## Service Manifest Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
  namespace: default
spec:
  type: ClusterIP
  selector:
    app: backend-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

---

## Ingress Controller & Routing

An Ingress manages external HTTP/HTTPS routing into services within the cluster:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: backend-service
                port:
                  number: 80
```

