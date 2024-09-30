import os
import time
import tensorflow as tf
from EcoMeal.entity.config_entity import PrepareCallbacksConfig

class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    def create_tensorboard_callbacks(self):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
        tensorboard_callback_log_dir = os.path.join([
            self.config.tensorboard_callback_log_dir, 
            f'tb_log_at_{timestamp}'
        ])
        return tf.keras.callbacks.Tensorboard(log_dir= tensorboard_callback_log_dir)
    
    def create_checkpoint_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath= self.config.checkpoint_model_filepath,
            save_weights_only= True,
            monitor= 'val_accuracy',
            mode= 'max',
            save_best_only= True
        )
    
    def get_tb_ckpt_callbacks(self):
        return [
            self.create_tensorboard_callbacks(), 
            self.create_checkpoint_callbacks()
        ]