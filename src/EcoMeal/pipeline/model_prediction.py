import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # List of dish names
        self.dish_names = [
            "Adhirasam", "Aloo Gobi", "Aloo Matar", "Aloo Methi", "Aloo Shimla Mirch",
            "Aloo Tikki", "Anarsa", "Ariselu", "Bandar Laddu", "Basundi",
            "Bhatura", "Bhindi Masala", "Biryani", "Boondi", "Butter Chicken",
            "Chak Hao Kheer", "Cham Cham", "Chana Masala", "Chapati", "Chhena Kheeri",
            "Chicken Razala", "Chicken Tikka", "Chicken Tikka Masala", "Chikki", "Daal Baati Churma",
            "Daal Puri", "Dal Makhani", "Dal Tadka", "Dharwad Pedha", "Doodhpak",
            "Double Ka Meetha", "Dum Aloo", "Gajar Ka Halwa", "Gavvalu", "Ghevar",
            "Gulab Jamun", "Imarti", "Jalebi", "Kachori", "Kadai Paneer",
            "Kadhi Pakoda", "Kajjikaya", "Kakinada Khaja", "Kalakand", "Karela Bharta",
            "Kofta", "Kuzhi Paniyaram", "Lassi", "Ledikeni", "Litti Chokha",
            "Lyangcha", "Maach Jhol", "Makki Di Roti Sarson Da Saag", "Malapua", "Misi Roti",
            "Misti Doi", "Modak", "Mysore Pak", "Naan", "Navrattan Korma",
            "Palak Paneer", "Paneer Butter Masala", "Phirni"
        ]

    def predict(self):
        model = load_model(os.path.join("artifacts", "model_training", "model.keras"))

        imagename = self.filename
        test_image = load_img(imagename, target_size=(224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        result = np.argmax(model.predict(test_image), axis=1)
        dish_name = self.dish_names[result[0]]  # Get the actual dish name from the index
        return [{"image": f"Predicted dish: {dish_name}"}]
