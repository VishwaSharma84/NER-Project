from datasets import load_dataset
from ner.exception import CustomException
from ner.logger import logging
import sys,os
from ner.config.configuration import Configuration
from ner.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config = data_ingestion_config
        
    def get_data(self):
        try:
            """
            This is class is responsible for data collection from official hugging face library.
            Cross-lingual Transfer Evaluation of Multilingual Encoders 
            (XTREME) benchmark called WikiANN or PAN-X.
            
            Returns: Dict of train test validation data 
            """

            logging.info("Loading data from hugging face")
            pan_en_data = load_dataset(self.data_ingestion_config.dataset_name,
                                       self.data_ingestion_config.subset_name,
                                       cache_dir= self.data_ingestion_config.data_path)
            logging.info(f"Dataset Info : {pan_en_data}")
            
            return pan_en_data
            
        except Exception as e:
            raise CustomException(e,sys) from e  