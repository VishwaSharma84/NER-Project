from ner.entity.config_entity import DataIngestionConfig
from ner.exception import CustomException
from ner.logger import logging
from ner.constant import *
from from_root import from_root
import sys,os
from ner.utils import read_yaml_file

class Configuration:
    def __init__(self, config_file_path = CONFIG_FILE_PATH) -> None:
        try:
            logging.info("Reading yaml file.....")
            self.config_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise CustomException(e,sys) from e    
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            artifacts_dir = os.path.join(ROOT_DIR,self.config_info[ARTIFACTS_DIR_KEY])
            
            dataset_name = self.config_info[DATA_INGESTION_KEY][DATASET_NAME]
            subset_name = self.config_info[DATA_INGESTION_KEY][SUBSET_NAME]
            data_store = os.path.join(self.config_info[ARTIFACTS_DIR_KEY],self.config_info[DATA_INGESTION_KEY][DATA_STORE_KEY])
            
            data_ingestion_config = DataIngestionConfig(
                dataset_name = dataset_name,
                subset_name=subset_name,
                data_path=data_store
            )
            
            return data_ingestion_config
            
        except Exception as e:
            raise CustomException(e,sys) from e
            