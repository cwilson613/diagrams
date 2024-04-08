# FluxCD Deployment Workflow

This diagram demonstrates the FluxCD workflow, which automatically synchronizes and applies changes from a Git repository to a Kubernetes cluster. FluxCD actively monitors the repository, applies the changes through a reconciliation process, and manages the lifecycle of applications within the cluster while providing feedback and monitoring.

```mermaid
graph TD
    A[Git Repository] -->|New Commit| B[FluxCD Sync]
    B -->|Reconciliation| C[Kubernetes Cluster]
    C --> D[Automated Deployment]
    D --> E[Health Checks]
    E -->|Status Report| F[Alerting & Monitoring]
    F -->|Monitor & Feedback| A
    A -->|Continuous Monitoring| B

    classDef git fill:#ffffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef flux fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef k8s fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef default fill:#ffcccc,stroke:#333,stroke-width:2px, color:#333;
    
    class A git;
    class B,C flux;
    class D,E,F k8s;
```