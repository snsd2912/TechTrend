# Helm Chart 

## Install

References here: https://helm.sh/docs/intro/install/

## Test

```
helm install [NAME] [CHART] [flags]
```

Example:
```
helm install techtrends ./template --values values-staging.yaml
```

## Issues

- Error:
```
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "http://localhost:8080/version": dial tcp 127.0.0.1:8080: connect: connection refused
```

- It happens because you're using K3s, so here is how to fix:
```
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```