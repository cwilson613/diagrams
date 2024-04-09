# GitLab CI/CD Pipeline for Terraform and FluxCD

This document illustrates the GitLab CI/CD pipeline designed for deploying infrastructure as code (IaC) with Terraform to provision AWS resources, including an EKS cluster. It also details the bootstrapping of FluxCD to deploy necessary platform applications on Kubernetes.

## Pipeline Diagram

```mermaid
graph TD
    A[Code Commit] -->|Trigger Pipeline| B[Lint Code]
    B --> C[Unit Tests]
    C --> D[Terraform Plan]
    D -->|Review Plan| E[Manual Approval]
    E -->|Apply Changes| F[Terraform Apply]
    F -->|Provision AWS Resources| G[Setup EKS Cluster]
    G --> H[Configure EKS]
    H --> I[Bootstrap FluxCD]
    I --> J[Deploy Applications]
    J --> K[Post-Deployment Tests]

    classDef startend fill:#f4c2c2,stroke:#333,stroke-width:2px, color:#333;
    classDef operation fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef approval fill:#ffcccc,stroke:#333,stroke-width:2px, color:#333;
    classDef deployment fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef test fill:#ffffcc,stroke:#333,stroke-width:2px, color:#333;

    class A startend;
    class B,C operation;
    class D,E approval;
    class F,G,H,I,J deployment;
    class K test;
```

## Explanation of Pipeline Components

- **Code Commit**: Initiates the CI/CD process, triggered by a commit to the repository.
- **Lint Code**: Performs static code analysis to ensure code quality and adherence to standards.
- **Unit Tests**: Executes unit tests to validate the functionality of the code before any deployment occurs.
- **Terraform Plan**: Generates an execution plan for Terraform, which allows developers and operations teams to review what Terraform will do before it makes any changes to the infrastructure.
- **Manual Approval**: Acts as a checkpoint requiring manual review and approval of the Terraform plan to ensure that all changes meet the necessary standards and policies before proceeding.
- **Terraform Apply**: Applies the approved Terraform configuration to provision AWS resources, including setting up an EKS cluster.
- **Setup EKS Cluster**: Involves the initial configuration of the EKS cluster once it has been provisioned by Terraform.
- **Configure EKS**: Involves additional configurations for the EKS cluster, potentially including networking and security settings.
- **Bootstrap FluxCD**: Sets up FluxCD on the newly configured EKS cluster, enabling it to manage deployments automatically based on configurations stored in Git.
- **Deploy Applications**: Utilizes FluxCD to deploy the necessary Kubernetes applications as defined by the configurations in the repository.
- **Post-Deployment Tests**: Executes tests to verify that the applications are running correctly and interacting as expected within the Kubernetes environment.