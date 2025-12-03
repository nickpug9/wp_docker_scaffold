from pathlib import Path

def create_project_structure(inputs):
    # Base project directory
    project_root = Path("")
    db_folder = project_root / "init"
    site_folder = project_root / inputs["project_name"]  # site folder named same as project

    
    # Create directories
    project_root.mkdir(parents=True, exist_ok=True)
    db_folder.mkdir(parents=True, exist_ok=True)
    site_folder.mkdir(parents=True, exist_ok=True)

    # Create docker-compose.yml placeholder
    # docker_compose_path = project_root / "docker-compose.yml"
    # with open(docker_compose_path, "w") as f:
    #     f.write("# Docker Compose configuration will be generated here\n")

    # Create README.md placeholder
    readme_path = project_root / "README.md"
    with open(readme_path, "w") as f:
        f.write(f"# {inputs['project_name']} Environment Setup\n\n")
        f.write("## How to start containers\n")
        f.write("```bash\ndocker-compose up -d\n```\n")
        f.write("## Folder Structure\n")
        f.write("- init/: Initial Database\n")
        f.write(f"- {inputs['project_name']}/: Site files\n")
    
    # Create .env with the input variables
    env_path = project_root / ".env"
    with open(env_path, "w") as f:
        for key, value in inputs.items():
            f.write(f"{key}={value}\n")

    print(f"✅ Project structure created at: {project_root.resolve()}")
    print(f"Folders: {db_folder}, {site_folder}")
    print(f"Files: {readme_path}, {env_path}")

    