from EcoMeal import logger
from EcoMeal.components.prepare_base_model import PrepareBaseModel
from EcoMeal.config.configurations import ConfigurationManager

STAGE_NAME = 'Prepare Base Model'
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f'Starting {STAGE_NAME}')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'Finished {STAGE_NAME}')
    except Exception as e:
        logger.exception(e)
        raise e