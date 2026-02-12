import os
from pathlib import Path

def import_site_directory(inputs):
    # If site repo is given, clone to project name folder
    if inputs["site_repo"]:
        os.system(f"git clone {inputs["site_repo"]} {inputs["project_name"]}")
        theme_folder = Path(inputs["project_name"]) / "wp-content" / "themes"
        # If theme repo given, clone to theme folder
        if inputs["theme_repo"]:
            os.system(f"git clone {inputs["theme_repo"]} {theme_folder}")