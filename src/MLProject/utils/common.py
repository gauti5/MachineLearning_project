# Utils --> those Functionality using frequently in our code


import os
from box.exceptions import BoxValueError
import yaml
from MLProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:    # Read lots of yaml file which present in the current project returned in ConfigBox
    """" reads yaml file and returns
    Args:
    path_to_yaml (str): path like input

    Raises:
    valueError: if yal file is empty
    e: empty file

    returns:
    ConfigBox: ConfigBox type

    """

    try:
        with open(path_to_yaml) as yaml_file:               # load a yaml file
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfylly")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    



@ensure_annotations
def create_directories(path_to_directoried: list, verbose=True):       # creating a Directories
    """Create list of directories
    Args:
    path_to_dirctories (list): list of path of directories
    ignore_log (bool, optional): ignore if mutliple dirs is to be created, default to false 

    """

    for path in path_to_directoried:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at; {path}")


@ensure_annotations
def save_json(path: Path,date: dict):
    """Save json Data
    Arsg:
    path(path): path to json file
    data(dict): data to be saved in json file
    
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json fles data
    
    Args : Path(path): path to  json file
    returns;
    ConfigBox: data as class attributes instead of dict
    """


    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file loaded successfullly from : {path}")
    return ConfigBox(content)


@ensure_annotations
def load_bin(path: path) ->Any:

    """Load binary Data
    Args: path(path):path to binary data
    returns: Any: object stored in the file
    """

    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args: path (path): Path of the file
    returns: str : Size in KB
    """



    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"


    