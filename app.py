from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open("parkinsons_model.pkl", "rb"))  # Ensure the model is saved in .pkl format

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # The frontend HTML file

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from the form
    data = request.form.to_dict(flat=True)
    data = pd.DataFrame([data], dtype=float)

    # Make prediction
    prediction = model.predict(data)[0]
    # Render prediction result in HTML
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
