import json
import numpy as np
import pandas as pd
import tensorflow as tf
from azureml.core.model import Model
from tensorflow.keras.models import load_model

# Initialize the model
def init():
    global model
    # Retrieve the model path from AzureML
    model_path = Model.get_model_path('stock_market_predict')  # Replace 'my_keras_model' with your model name
    # Load the Keras model
    model = load_model(model_path)

# Predict
def run(raw_data):
    try:
        # Convert raw data to a DataFrame
        data = pd.read_json(raw_data)
        
        # Ensure data is in the right format for your model
        # Example: If your model expects a 2D array
        data_array = np.array(data)

        # Make predictions
        predictions = model.predict(data_array)

        # Convert predictions to a list and then to JSON
        predictions_list = predictions.tolist()
        return json.dumps(predictions_list)
    except Exception as e:
        error = str(e)
        return json.dumps({"error": error})
