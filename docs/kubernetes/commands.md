# ☸️ Kubernetes (K8s) Commands Cheat Sheet

A comprehensive, production-ready reference guide for Kubernetes CLI (`kubectl`) commands, structured by domain and usage pattern.

---

## 📌 Table of Contents

1. [Cluster Info & Health](#1-cluster-info-health)
2. [Pod Management](#2-pod-management)
3. [Deployments & Workloads](#3-deployments-workloads)
4. [Services & Networking](#4-services-networking)
5. [ConfigMaps & Secrets](#5-configmaps-secrets)
6. [Namespaces](#6-namespaces)
7. [Nodes & Resource Monitoring](#7-nodes-resource-monitoring)
8. [Debugging & Troubleshooting](#8-debugging-troubleshooting)
9. [RBAC & Security](#9-rbac-security)
10. [Imperative Shortcuts & Useful One-Liners](#10-imperative-shortcuts-useful-one-liners)

---

## 1. Cluster Info & Health

Commands to inspect the cluster control plane, context, and overall status.

| Command | Description |
| :--- | :--- |
| `kubectl cluster-info` | Display endpoint information for the master and services. |
| `kubectl version --short` | Show client and server Kubernetes versions. |
| `kubectl config get-contexts` | List all available cluster contexts. |
| `kubectl config current-context` | Display the current active context. |
| `kubectl config use-context <context-name>` | Switch to a different cluster context. |
| `kubectl config set-context --current --namespace=<namespace>` | Set default namespace for the current context. |
| `kubectl get componentstatuses` (or `get cs`) | Check health of control plane components (etcd, scheduler, controller-manager). |

---

## 2. Pod Management

Pods are the smallest execution units in Kubernetes.

### Listing & Inspecting

```bash
# List all pods in default namespace
kubectl get pods

# List pods with detailed information (IP, Node name, status)
kubectl get pods -o wide

# List pods across ALL namespaces
kubectl get pods --all-namespaces

# Get live stream of pod status changes
kubectl get pods -w

# Describe a specific pod to view event logs and detailed state
kubectl describe pod <pod-name>

# Output pod manifest as YAML
kubectl get pod <pod-name> -o yaml
```

### Creating & Managing

```bash
# Run an imperative NGINX pod
kubectl run nginx --image=nginx:alpine

# Run an interactive temporary debugging pod
kubectl run -i --tty busybox --image=busybox --restart=Never -- sh

# Delete a pod immediately (force remove)
kubectl delete pod <pod-name> --grace-period=0 --force
```

---

## 3. Deployments & Workloads

Deployments manage declarative updates for Pods and ReplicaSets.

| Task | Command |
| :--- | :--- |
| **Create Deployment** | `kubectl create deployment web-app --image=nginx:1.21` |
| **List Deployments** | `kubectl get deployments` |
| **Scale Replicas** | `kubectl scale deployment web-app --replicas=5` |
| **Autoscale (HPA)** | `kubectl autoscale deployment web-app --min=2 --max=10 --cpu-percent=80` |
| **Update Image** | `kubectl set image deployment/web-app nginx=nginx:1.23` |
| **View Rollout History** | `kubectl rollout history deployment/web-app` |
| **Rollback Update** | `kubectl rollout undo deployment/web-app` |
| **Pause Rollout** | `kubectl rollout pause deployment/web-app` |
| **Resume Rollout** | `kubectl rollout resume deployment/web-app` |
| **Check Rollout Status** | `kubectl rollout status deployment/web-app` |

---

## 4. Services & Networking

Services expose Pods to internal or external traffic.

```bash
# Expose a deployment as a ClusterIP service (Internal)
kubectl expose deployment web-app --port=80 --target-port=8080 --type=ClusterIP --name=web-service

# Expose a deployment as a NodePort service (External via Node IP)
kubectl expose deployment web-app --port=80 --type=NodePort --name=web-service-node

# Expose as LoadBalancer (Cloud-managed external IP)
kubectl expose deployment web-app --port=80 --type=LoadBalancer --name=web-lb

# List all services with assigned IPs and Ports
kubectl get svc -o wide

# Get Endpoint mappings for services
kubectl get endpoints

# List Ingress rules
kubectl get ingress
```

---

## 5. ConfigMaps & Secrets

Store configuration data and confidential credentials decoupled from container images.

### ConfigMaps

```bash
# Create ConfigMap from literal values
kubectl create configmap app-config --from-literal=DB_HOST=10.0.0.1 --from-literal=DB_PORT=5432

# Create ConfigMap from a file
kubectl create configmap app-config --from-file=config.properties

# View ConfigMap content
kubectl get configmap app-config -o yaml
```

### Secrets

```bash
# Create generic Secret from literal values
kubectl create secret generic db-pass --from-literal=password='SuperSecret123!'

# Create TLS secret from key/cert files
kubectl create secret tls web-tls --cert=path/to/tls.crt --key=path/to/tls.key

# View secret data (Base64 encoded)
kubectl get secret db-pass -o yaml
```

---

## 6. Namespaces

Isolate resources within a physical cluster.

```bash
# List all namespaces
kubectl get namespaces

# Create a new namespace
kubectl create namespace staging

# Run a pod in a specific namespace
kubectl run test-pod --image=nginx -n staging

# Get resources across a specific namespace
kubectl get all -n staging

# Delete a namespace (Deletes all resources inside it!)
kubectl delete namespace staging
```

---

## 7. Nodes & Resource Monitoring

Monitor cluster node health and resource utilization.

```bash
# List all cluster nodes
kubectl get nodes -o wide

# Describe node details (Capacity, Allocatable, Taints, Conditions)
kubectl describe node <node-name>

# Cordon a node (Mark as unschedulable)
kubectl cordon <node-name>

# Uncordon a node (Mark as schedulable)
kubectl uncordon <node-name>

# Drain node gracefully in preparation for maintenance
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# View resource usage (CPU/Memory) for Nodes (Requires Metrics Server)
kubectl top nodes

# View resource usage (CPU/Memory) for Pods
kubectl top pods --all-namespaces
```

---

## 8. Debugging & Troubleshooting

Essential diagnostics for failing workloads.

```bash
# Fetch container logs
kubectl logs <pod-name>

# Stream live container logs (Follow mode)
kubectl logs -f <pod-name>

# Fetch logs for a specific container in a multi-container pod
kubectl logs <pod-name> -c <container-name>

# Fetch logs of a previously crashed container instance
kubectl logs <pod-name> --previous

# Execute interactive shell command inside a running pod
kubectl exec -it <pod-name> -- /bin/sh

# Port-forward a local port to a pod port (Local testing)
kubectl port-forward pod/<pod-name> 8080:80

# Port-forward to a service
kubectl port-forward svc/<service-name> 8080:80

# View detailed events ordered by timestamp
kubectl get events --sort-by='.metadata.creationTimestamp'
```

---

## 9. RBAC & Security

Check permissions and manage access controls.

```bash
# Check if current user can perform an action
kubectl auth can-i create pods
kubectl auth can-i delete nodes

# Check if a specific service account can perform an action
kubectl auth can-i get secrets --as=system:serviceaccount:default:my-sa

# View ServiceAccounts
kubectl get serviceaccounts (or `get sa`)

# View Roles and ClusterRoles
kubectl get roles,clusterroles

# View RoleBindings and ClusterRoleBindings
kubectl get rolebindings,clusterrolebindings
```

---

## 10. Imperative Shortcuts & Useful One-Liners

Fast track commands to quickly generate manifests and clean up resources.

### DRY-RUN Manifest Generation (No cluster creation)

```bash
# Generate Pod YAML
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml

# Generate Deployment YAML
kubectl create deployment web --image=nginx --dry-run=client -o yaml > deployment.yaml

# Generate Service YAML
kubectl create service clusterip web --tcp=80:8080 --dry-run=client -o yaml > service.yaml
```

### Rapid Cleanup & Management

```bash
# Delete all evicted pods
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " --namespace=" $1}' | xargs kubectl delete pod

# Quickly delete resources declared in a manifest directory
kubectl delete -f ./manifests/

# Apply all manifests in a directory recursively
kubectl apply -f ./manifests/ -R
```

---
