from EcoMeal import logger
from EcoMeal.pipeline.data_ingestion import DataIngestionTrainingPipeline
from EcoMeal.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f'Starting {STAGE_NAME} stage')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'Finished {STAGE_NAME} stage')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f'Starting {STAGE_NAME} stage')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'Finished {STAGE_NAME} stage')
except Exception as e:
    logger.exception(e)
    raise e