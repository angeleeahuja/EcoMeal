from EcoMeal import logger
from EcoMeal.components.model_evaluation import ModelEvaluation
from EcoMeal.config.configurations import ConfigurationManager

STAGE_NAME = 'Model Evaluation'
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.evaluate_model()
        model_evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f'Starting {STAGE_NAME}')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'Finished {STAGE_NAME}')
    except Exception as e:
        logger.exception(e)
        raise e