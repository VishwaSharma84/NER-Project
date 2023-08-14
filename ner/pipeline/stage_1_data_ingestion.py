from ner.components.data_ingestion import DataIngestion
from ner.config.configuration import Configuration
from ner.exception import CustomException
from ner.logger import logging
import sys,os

STAGE_NAME = "Data Ingestion stage"

def main():
    config = Configuration()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.get_data()

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys) from e