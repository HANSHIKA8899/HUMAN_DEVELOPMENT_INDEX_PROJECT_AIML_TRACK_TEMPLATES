from flask import Flask, request, render_template
import pickle
import numpy as np
import os
print("Current Folder: ", os.getcwd())
print("Files:", os.listdir())
app = Flask(__name__)
model = pickle.load(open('HDI.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/prediction')
def prediction():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    hdi = prediction[0][0]

    if hdi < 0.550:
        category = "🔴 Low Human Development"
        recommendations = [
            "Improve access to quality healthcare.",
            "Increase school enrollment and literacy.",
            "Develop basic infrastructure.",
            "Create more employment opportunities.",
            "Improve access to clean water and sanitation."
        ]

    elif hdi < 0.700:
        category = "🟡 Medium Human Development"
        recommendations = [
            "Improve higher education quality.",
            "Strengthen healthcare services.",
            "Promote vocational and technical training.",
            "Increase employment opportunities.",
            "Support rural development programs."
        ]

    elif hdi < 0.800:
        category = "🔵 High Human Development"
        recommendations = [
            "Invest in research and innovation.",
            "Improve digital literacy.",
            "Promote sustainable development.",
            "Enhance higher education.",
            "Reduce income inequality."
        ]

    else:
        category = "🟢 Very High Human Development"
        recommendations = [
            "Maintain healthcare excellence.",
            "Promote green technologies.",
            "Encourage innovation and R&D.",
            "Improve quality of life.",
            "Strengthen environmental sustainability."
        ]
    return render_template('index.html', prediction_text=f'🌍 Predicted Human Development Index (HDI): {prediction[0][0]:.4f}', category=category, recommendations=recommendations)
if __name__ == "__main__":
    app.run(debug=True)