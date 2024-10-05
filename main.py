from ecomeal import logger
from ecomeal.pipeline.data_ingestion import DataIngestionTrainingPipeline
from ecomeal.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from ecomeal.pipeline.model_training import ModelTrainingPipeline
from ecomeal.pipeline.model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f'Starting {STAGE_NAME}')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'Finished {STAGE_NAME}')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f'Starting {STAGE_NAME}')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'Finished {STAGE_NAME}')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f" Starting {STAGE_NAME}")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'
try:
    logger.info(f" Starting {STAGE_NAME}")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e