import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

from pathlib import Path
import tensorflow as tf
from EcoMeal.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg19.VGG19(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top = self.config.params_include_top
        )
        self.save_model(path= self.config.base_model_path, model= self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False
        
        flatten_in = tf.keras.layers.Flatten()(model.output)
        dense_layer = tf.keras.layers.Dense(units=512, activation='relu')(flatten_in)
        dense_layer = tf.keras.layers.BatchNormalization()(dense_layer)
        dense_layer = tf.keras.layers.Dropout(0.5)(dense_layer)

        dense_layer = tf.keras.layers.Dense(units=256, activation='relu')(dense_layer)
        dense_layer = tf.keras.layers.BatchNormalization()(dense_layer)
        dense_layer = tf.keras.layers.Dropout(0.5)(dense_layer)

        dense_layer = tf.keras.layers.Dense(units=128, activation='relu')(dense_layer)
        dense_layer = tf.keras.layers.BatchNormalization()(dense_layer)
        dense_layer = tf.keras.layers.Dropout(0.5)(dense_layer)

        prediction = tf.keras.layers.Dense(units=classes, activation='softmax')(dense_layer)
        
        full_model = tf.keras.models.Model(
            inputs= model.input,
            outputs= prediction
        )

        full_model.compile(
            optimizer= tf.keras.optimizers.Adam(learning_rate= learning_rate),
            loss= tf.keras.losses.CategoricalCrossentropy(),
            metrics= ['accuracy']
        )

        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model= self.model,
            classes= self.config.params_classes,
            freeze_all= True,
            freeze_till= None,
            learning_rate= self.config.params_learning_rate
        )

        self.save_model(path= self.config.updated_base_model_path, model= self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        # if not path.suffix == '.keras':
        #     path = path.with_suffix('.keras')
        model.save(path, include_optimizer=False)