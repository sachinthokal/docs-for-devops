# Kubernetes Volumes & Persistent Storage

Managing stateful workloads, volumes, PersistentVolumes (PV), PersistentVolumeClaims (PVC), and StorageClasses in Kubernetes.

---

## Storage Architecture

```
[ Pod Container ] 
       │
       ▼ (Volume Mount)
[ PersistentVolumeClaim (PVC) ] ── (Requests Storage) ──► [ StorageClass ]
       │                                                         │
       ▼ (Bound To)                                              ▼
[ PersistentVolume (PV) ] ◄───────────────────────── (Dynamic Provisioning)
       │
       ▼
[ Cloud / Block Storage ] (EBS / Azure Disk / NFS / Ceph)
```

---

## PersistentVolumeClaim (PVC)

Applications request physical storage capacity and access modes without coupling to specific cloud storage backends:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: database-storage-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard-ssd
  resources:
    requests:
      storage: 20Gi
```

### Access Modes

- **ReadWriteOnce (RWO)**: Volume can be mounted as read-write by a single node.
- **ReadOnlyMany (ROX)**: Volume can be mounted read-only by many nodes.
- **ReadWriteMany (RWX)**: Volume can be mounted read-write by many nodes concurrently (e.g. NFS, EFS).
- **ReadWriteOncePod (RWOP)**: Volume can be mounted as read-write by a single pod exclusively (introduced in Kubernetes v1.22+).

