import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  #Want to see Log in the terminal

# What kind of Log it is ( Above Line is about Logging Information, timestamp, Error Message)

project_name= "MLProject"

list_of_files=[
    ".github/workflows/.gitkeep",                # Creating a new folder .github, inside another folder worflows and .gitkeep file.
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # Arranging the folders first it will create a MLProject Folder --> Components Folder -->__init__.py file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    'params.yaml',
    "schema.yaml",
    "main.py",
    "app.py"
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "test.py"
]


for filepath in list_of_files:                  
    filepath=Path(filepath)
    filedir, filename =os.path.split(filepath)    # Spliting the above folders storing in seperate variable and file in separte variable

    if filedir != "":                             # if the folder directory is not empty the create a folder structure
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")   # Logging the Information
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # Checking the file path exists and if path is zero then create the file
        with open(filepath, "w") as f:
            pass 
        logging.info(f"Creating empty file: {filepath}")  # Log the information

    else:
        logging.info("f{filename} is already exists")        #if everything is ok then try to give the file name is already exists.





