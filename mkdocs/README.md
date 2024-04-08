
# MkDocs with Mermaid Integration Guide

## Step 1: Set Up Your Project

First, install MkDocs and the Mermaid plugin using pip:

```bash
pip install mkdocs
pip install mkdocs-mermaid2-plugin
```

## Step 2: Create Your MkDocs Project

Initialize a new MkDocs project if starting fresh:

```bash
mkdocs new nce-platform-docs
cd nce-platform-docs
```

## Step 3: Configure MkDocs

Edit the `mkdocs.yml` file to include the Mermaid plugin:

```yaml
site_name: NCE Platform Documentation
plugins:
  - search
  - mermaid2

theme:
  name: material
```

## Step 4: Prepare Your Documentation

Place your `.mmd` files in a directory, such as `diagrams/`, and create Markdown files in your `docs/` directory.

## Step 5: Write Markdown with Embedded Mermaid Diagrams

Include Mermaid diagrams directly in your Markdown files:

```markdown
# Example Diagram

Here is an example of a Mermaid diagram included directly:

    ```mermaid
    graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
    ```
```
Or use a script to insert `.mmd` file contents into Markdown before building your docs.

## Step 6: Build and Serve Your Documentation

Build your documentation:

```bash
mkdocs build
```

Or serve it locally:

```bash
mkdocs serve
```

Access your documentation at `http://127.0.0.1:8000`.

TODO:
- test references and what relative paths can be used to import the diagrams (i.e. must it be child dir of mkdocs?)
- submodules for drawio?
- drawio mkdocs integration?
