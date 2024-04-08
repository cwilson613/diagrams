# Istio Service Mesh on EKS

Explanation of the Diagram Components

- EKS Cluster: The overall Kubernetes cluster managed by EKS.
- Istio Control Plane: Manages Istio's operational logic, including traffic management, policies, and configuration.
- Kubernetes Nodes: Physical or virtual machines that host Kubernetes pods.
- Envoy Sidecars: Deployed alongside each service pod to manage network communication.
- Pods: Contains one or more containers (including Envoy proxies when Istio is used).
- Services: Kubernetes Services that abstract the logic of pod access.
- Service Discovery: Component of Istio that handles the discovery of services within the mesh.
- Ingress Gateway: Manages access to the services from external sources.
- Access Control: Policies enforced by the sidecars for service-to-service communication.
- Telemetry: Collection of metrics and logging data facilitated by the sidecars.

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
```