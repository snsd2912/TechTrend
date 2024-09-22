# ArgoCD Manifests 

## Install

Refer to: https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd

### ArgoCD UI

After all the resources are up and running, run the below using argoci cli to get initial password to login to ArgoCD UI:
```
argocd admin initial-password -n argocd
```

You can port fowarding to access ArgoCD UI from local using:
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Alnatively, create a NodePort service using the argocd-server-nodeport.yaml file, it will expose ArgoCD UI. In this way, we don't have to use port-forward multiple times.

```
kubectl apply -f argocd-server-nodeport.yaml
```

## How ArgoCD works

ArgoCD is a declarative GitOps tool for managing Kubernetes applications.

1. Project
- Purpose: ArgoCD Projects are a way to organize and manage multiple applications. They allow you to group related applications under a common security boundary and apply policies.
- Key Features:
    - Namespace and Resource Management: Projects can define which Kubernetes namespaces and clusters an application can be deployed to.
    - Access Controls: Policies can be set to restrict who can manage or access applications within a project.
    - Cluster and Repo Restrictions: Projects can restrict which repositories and clusters an application can use, providing an additional security layer.
- Use Case: You might create a "Staging" project and a "Production" project to manage applications in different environments separately.

2. Repository
- Purpose: A repository is where the application manifests (YAML files, Helm charts, Kustomize configs, etc.) are stored. ArgoCD continuously monitors these repositories for changes.
- Supported Types: ArgoCD supports Git repositories, Helm repositories, and Kustomize sources.
- Key Features:
    - Source of Truth: The repository serves as the single source of truth for your application configuration. Every change is tracked through Git, providing an audit trail.
    - Automatic Syncing: ArgoCD can automatically synchronize your Kubernetes cluster to the desired state defined in the repository, ensuring that your cluster reflects what’s in the Git repository.
- Use Case: You would connect a Git repository containing Kubernetes manifests for different environments (like staging and production), and ArgoCD will sync the cluster based on these definitions.

3. Application
- Purpose: An ArgoCD Application represents a single Kubernetes application that is defined in a Git repository. It tells ArgoCD where to find the manifests and how to deploy them.
- Key Features:
    - Declarative Syncing: The application defines which repository, path, and cluster to sync, and it ensures the application is deployed and kept up to date.
    - Helm and Kustomize Support: Applications can use Helm charts, Kustomize patches, or plain YAML manifests for their configuration.
    - Monitoring and Health Management: ArgoCD constantly monitors the state of the application in the cluster. If the desired state (defined in the Git repository) and the actual state (in the cluster) drift, ArgoCD can alert you or automatically reconcile the difference.
    - Rollbacks and Rollouts: Applications support versioning, allowing you to easily roll back to a previous version if needed.
- Use Case: For example, you might define an ArgoCD application for a microservice, linking it to the appropriate Helm chart or Kubernetes manifests stored in your Git repository.

### Flow Example

- Project: Create a project for "Staging" and set policies that allow certain applications to be deployed.
- Repository: Define a Git repository containing your Kubernetes manifests (like values-staging.yaml for Helm charts).
- Application: Create an ArgoCD Application that links to the repository, specifies the correct cluster and namespace, and syncs your deployment.


