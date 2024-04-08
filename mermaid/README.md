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

