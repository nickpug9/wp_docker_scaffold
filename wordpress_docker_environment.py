import argparse
import os
from getpass import getpass
from create_project_structure import create_project_structure


# Scaffold the docker environment to clone a live website

# STEPS to take:
# 1. Prompt for inputs
# 2. Create folder structure
# project-root/
# ├── docker-compose.yml
# ├── init/
# ├── README.md
# ├── .env
# └── site/ (optional)
# 3. Generate files (docker-compose.yml, .env, README.md)
# 4. Fetch latest DB Backup
# 5. Optional: Clone site repo
# 6. Print next steps (how to start, how to import db)

# Prompt for inputs
def get_inputs():
    print("=== Docker Scaffolding Setup ===")

    project_name = input("Enter project name: ")
    db_name = input("Enter database name: ")
    db_user = input("Enter database user: ")
    db_password = getpass("Enter database password: ")
    db_root_password = getpass("Enter database root password: ")
    wp_port = input("Enter WordPress port (default 8080): ") or "8080"
    myadmin_port = input("Enter phpmyadmin port (default 8081): ") or "8080"

    backup_url = input("Enter backup URL (leave blank to skip): ")
    site_repo = input("Enter site repo URL (leave blank to skip): ")
    if site_repo:
        theme_repo = input("Enter theme repo URL (leave blank to skip): ")


    return {
        "project_name": project_name,
        "db_name": db_name,
        "db_user": db_user,
        "db_password": db_password,
        "db_root_password": db_root_password,
        "wp_port": wp_port,
        "myadmin_port": myadmin_port,
        "backup_url": backup_url if backup_url else None,
        "site_repo": site_repo if site_repo else None,
        "theme_repo": theme_repo if theme_repo else None
    }

if __name__ == "__main__":
    inputs = get_inputs()
    create_project_structure(inputs)

    
