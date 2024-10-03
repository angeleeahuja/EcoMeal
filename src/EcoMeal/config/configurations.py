import os
from EcoMeal.constants import *
from EcoMeal.utils.common import read_yaml, create_directories
from EcoMeal.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, 
                                          ModelTrainingConfig, ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(self, config_path= CONFIG_FILE_PATH, params_path= PARAMS_FILE_PATH):
        self.config= read_yaml(config_path)
        self.params= read_yaml(params_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        di_config = self.config.data_ingestion
        create_directories([di_config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir= di_config.root_dir,
            source_url= di_config.source_url,
            local_data_file= di_config.local_data_file,
            unzip_dir= di_config.unzip_dir
        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        bm_config = self.config.prepare_base_model
        create_directories([bm_config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir= Path(bm_config.root_dir),
            base_model_path= Path(bm_config.base_model_path),
            updated_base_model_path = Path(bm_config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_classes= self.params.CLASSES
        )
        return prepare_base_model_config
    
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        cb_config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(cb_config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(cb_config.tensorboard_root_log_dir)
        ])

        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir= Path(cb_config.root_dir),
            tensorboard_root_log_dir = Path(cb_config.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(cb_config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        model_training = self.config.model_training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'Indian Food Images')
        create_directories([Path(model_training.root_dir)])

        model_training_config = ModelTrainingConfig(
            root_dir= Path(model_training.root_dir),
            trained_model_path= Path(model_training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_is_augumentation= params.AUGUMENTATION,
            params_image_size= params.IMAGE_SIZE
        )
        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        model_training = self.config.model_training
        evaluation_config = ModelEvaluationConfig(
            model_path= Path(model_training.trained_model_path),
            training_data_path= Path("artifacts\data_ingestion\Indian Food Images"),
            all_params= self.params,
            params_batch_size= self.params.BATCH_SIZE,
            params_image_size= self.params.IMAGE_SIZE
        )
        return evaluation_config