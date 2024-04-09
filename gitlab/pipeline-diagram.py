import yaml
import os
import re

def read_yaml(file_path):
    """Read and parse a YAML file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_mermaid_diagram(pipeline_data):
    """Generate a Mermaid diagram from the pipeline data."""
    diagram = "graph TD\n"
    nodes = set()
    links = []

    # Process each job to determine nodes and links
    for job_name, job_details in pipeline_data.items():
        if isinstance(job_details, dict):
            stage = job_details.get('stage', 'default').replace(" ", "_")
            job_node = job_name.replace(" ", "_")

            # Ensure all nodes are unique
            nodes.add(f'{stage}["Stage: {stage}"]')
            nodes.add(f'{job_node}["Job: {job_name}"]')
            links.append(f'{stage} --> {job_node}')

            # Handle dependencies if specified
            if 'dependencies' in job_details:
                for dependency in job_details['dependencies']:
                    dep_node = dependency.replace(" ", "_")
                    links.append(f'{dep_node} --> {job_node}')
            elif 'needs' in job_details:
                for need in job_details['needs']:
                    if isinstance(need, dict):
                        need = need.get('job')
                    need_node = need.replace(" ", "_")
                    links.append(f'{need_node} --> {job_node}')

    # Add nodes and links to the diagram
    for node in nodes:
        diagram += f'    {node}\n'
    for link in links:
        diagram += f'    {link}\n'

    return diagram

def create_markdown(diagram, output_file='output.md'):
    """Create a Markdown file with the diagram."""
    content = f"# Pipeline Diagram\n\n```mermaid\n{diagram}```\n"
    with open(output_file, 'w') as file:
        file.write(content)
    print(f"Markdown file created: {output_file}")

def main():
    yaml_path = './.gitlab-docker-example-pipeline.yml'  # Update this path
    md_path = re.sub('.yml', '.md', os.path.basename(yaml_path))
    pipeline_data = read_yaml(yaml_path)
    mermaid_diagram = generate_mermaid_diagram(pipeline_data)
    create_markdown(mermaid_diagram, output_file=md_path)

if __name__ == "__main__":
    main()
