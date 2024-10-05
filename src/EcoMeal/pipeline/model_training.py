from ecomeal import logger
from ecomeal.components.model_training import ModelTraining
from ecomeal.components.prepare_callbacks import PrepareCallbacks
from ecomeal.config.configurations import ConfigurationManager

STAGE_NAME = 'Model Training Stage'
class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_model_training_config()
        training = ModelTraining(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)

if __name__ == '__main__':
    try:
        logger.info(f" Starting {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Finshed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
        