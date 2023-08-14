import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()
CONFIG_DIR = "configs"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)


ARTIFACTS_DIR_KEY = "artifacts"


DATA_INGESTION_KEY = "data_ingestion_config"
DATASET_NAME = "dataset_name"
SUBSET_NAME = "subset_name"
DATA_STORE_KEY = "data_store"
