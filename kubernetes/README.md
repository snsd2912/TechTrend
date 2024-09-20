## Kubernetes Declarative Manifests 

## Installation

### Install k3s master node

curl -sfL https://get.k3s.io | sh -

### Install k3s agent node

curl -sfL https://get.k3s.io | K3S_URL=https://<master-ip>:6443 K3S_TOKEN=<master-token> sh -

### Update agent node configuration

The agent node must have a valid kubeconfig file that points to the control plane (master node), which is responsible for the Kubernetes API. By default, the API server does not run on agent nodes in a Kubernetes cluster, so the kubectl command needs to contact the control plane.

On the master node (control plane):

```
sudo cat /etc/rancher/k3s/k3s.yaml
```

Copy this file to the agent node into ~/.kube/config, or set it as an environment variable like this:

```
export KUBECONFIG=/path/to/kubeconfig
```

**Noted**: You must update server's IP on the configuration


## Test

kubectl config set-context --current --namespace=sandbox

kubectl port-forward <pod-name> 8080:<pod-port> -n <namespace>

kubectl port-forward techtrends-7ff989b97d-68mkm 8080:3111