# Mermaid Diagrams

This README dynamically displays Mermaid diagrams found in the .mmd files within this directory.

## Diagram: mermaid/gitops-basic
```mermaid
graph TD
    A[Git Repository] -->|Code commit| B[CI Pipeline]
    B -->|Build & Test| C[Image Registry]
    C --> D[Deployment Pipeline]
    D -->|Deploy to Test Environment| E[Test Environment]
    D -->|Deploy to Prod Environment| F[Prod Environment]
    E --> G[Test Validation]
    G -->|Feedback| A
    F --> H[Monitoring & Logging]

    classDef git fill:#ffffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef ci fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef registry fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef deployment fill:#ffcccc,stroke:#333,stroke-width:2px, color:#333;
    classDef env fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef monitoring fill:#fff2cc,stroke:#333,stroke-width:2px, color:#333;

    class A git;
    class B ci;
    class C registry;
    class D deployment;
    class E,F env;
    class G,H monitoring;
```

## Diagram: mermaid/istio-eks-basic
```mermaid
graph TB
    A[EKS Cluster] -->|Hosts| B[Istio Control Plane]
    A -->|Hosts| C[Kubernetes Nodes]
    B -->|Configures| D[Envoy Sidecars]
    C -->|Runs| E[Pods]
    E -->|Injects| D
    D -->|Routes Traffic| E
    E -->|Communication| F[Services]
    F --> G[Service Discovery]
    F -->|Managed by| H[Ingress Gateway]
    H -->|Receives External Traffic| F
    G -->|Registers Services| F
    B -->|Manages Traffic Rules| D
    D -->|Enforces Policies| I[Access Control]
    D -->|Collects Metrics| J[Telemetry]

    classDef cluster fill:#ffffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef istio fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef k8s fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef sidecar fill:#ffcccc,stroke:#333,stroke-width:2px, color:#333;
    classDef services fill:#fff2cc,stroke:#333,stroke-width:2px, color:#333;
    classDef policy fill:#f9d5e5,stroke:#333,stroke-width:2px, color:#333;
    classDef telemetry fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;

    class A cluster;
    class B istio;
    class C k8s;
    class D sidecar;
    class E k8s;
    class F services;
    class G services;
    class H services;
    class I policy;
    class J telemetry;

    %% Legend
    L1[Legend:] --> L2[Cluster: EKS Cluster]
    L1 --> L3[Istio: Istio Control Plane]
    L1 --> L4[K8s: Kubernetes Nodes and Pods]
    L1 --> L5[Sidecar: Envoy Sidecars]
    L1 --> L6[Services: Kubernetes Services]
    L1 --> L7[Policy: Access Control]
    L1 --> L8[Telemetry: Telemetry Collection]

    class L1 legend;
    class L2,L3,L4,L5,L6,L7,L8 legend;

    classDef legend fill:#fff,stroke:#333,stroke-width:0px, color:#333;
```

