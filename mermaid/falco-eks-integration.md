# Falco Integration with AWS EKS

This diagram shows how Falco, a cloud-native runtime security project, integrates with AWS Elastic Kubernetes Service (EKS) to monitor and secure containerized applications at the kernel level. Falco taps into the Linux kernel to detect anomalous activities based on predefined rules and sends alerts, which can then be managed and responded to within the Kubernetes cluster environment.

```mermaid
graph TD
    A[Falco DaemonSet] -->|Installs on All Nodes| B[Linux Kernel]
    B -->|Monitors System Calls| C[Falco Engine]
    C -->|Rule Evaluation| D[Falco Rules]
    C -->|Generates Alerts| E[Falco Alerts]
    E -->|Output Channels| F[Alert Routing]
    F -->|Syslog, Slack, etc.| G[Notification Services]
    F -->|K8s Response Engine| H[Custom Responses]
    H -->|Patch, Scale, etc.| I[EKS Actions]
    
    classDef falco fill:#ffcccc,stroke:#333,stroke-width:2px, color:#333;
    classDef kernel fill:#ccccff,stroke:#333,stroke-width:2px, color:#333;
    classDef rules fill:#ccffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef alerts fill:#ffffcc,stroke:#333,stroke-width:2px, color:#333;
    classDef routing fill:#f9f7ed,stroke:#333,stroke-width:2px, color:#333;
    classDef actions fill:#f4c2c2,stroke:#333,stroke-width:2px, color:#333;

    class A,B falco;
    class C,D kernel;
    class E,F,G alerts;
    class H,I actions;
