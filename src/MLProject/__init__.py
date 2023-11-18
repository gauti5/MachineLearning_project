import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s : %(module)s: %(message)s]"

log_dir="Logs"                                              # Creating a Logs Folder...
log_filepath=os.path.join(log_dir,"running_logs.log")       # Inside a Logs Folder --> running_logs.log
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,


    handlers=[
        logging.FileHandler(log_filepath),   # Creates a Logs folder inside will happen all loggings...
        logging.StreamHandler(sys.stdout)    # print the Log in the terminal

    ]
)

logger=logging.getLogger("MLProjectLogger")      # intialize the Logging Folder (MlProjectLogger)