# Kubernetes Pod & Cluster Security

Hardening workloads and enforcing security boundaries using Pod Security Standards (PSS), Pod Security Admission (PSA), and SecurityContexts.

---

## Pod Security Standards (PSS)

Kubernetes classifies pod security into three progressive profiles:

1. **Privileged**: Unrestricted permissions; intended for system-level daemons, CNIs, and storage drivers.
2. **Baseline**: Minimally restrictive policy preventing known privilege escalations.
3. **Restricted**: Heavily hardened policy following modern cloud-native security best practices.

Enforced at namespace level using labels:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production-secured
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/warn: restricted
```

---

## Workload SecurityContext

Enforce immutable root filesystems, non-root users, and dropped capabilities:

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    fsGroup: 10001
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: api-workload
      image: ghcr.io/myorg/api:1.0.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
```

