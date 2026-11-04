# Kubernetes ConfigMaps & Secrets

Decoupling configuration artifacts and sensitive credentials from container image builds in Kubernetes.

---

## ConfigMaps

ConfigMaps store non-confidential key-value configuration data:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: default
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
  config.json: |
    {
      "timeout": 30,
      "retries": 3
    }
```

### Injecting into Pods

```yaml
spec:
  containers:
    - name: app
      image: nginx:alpine
      envFrom:
        - configMapRef:
            name: app-config
```

---

## Secrets

Secrets store small amounts of sensitive data (passwords, tokens, API keys). Kubernetes encodes values in base64:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
  namespace: default
type: Opaque
data:
  username: YWRtaW4= # echo -n "admin" | base64
  password: cGFzc3dvcmQxMjM= # echo -n "password123" | base64
```

### External Secrets Operator (ESO)

For enterprise security, integrate cloud secret managers (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) using the **External Secrets Operator** to synchronize secrets securely into Kubernetes native secrets without committing credentials to Git.

