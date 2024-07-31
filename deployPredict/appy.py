from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load your model here
model = tf.keras.models.load_model('finalModelPredict.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
