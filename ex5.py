from flask import Flask, request, render_template
import pandas as pd
import joblib


# Load saved model
obj = joblib.load("california.joblib")

model = obj["model"]
columns = obj["columns"]


# Create Flask app
app = Flask(__name__)


# Home page
@app.route("/")
def Main():

    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["GET"])
def predict():

    input_data = []

    for i in columns:

        # Get value from HTML form
        val = request.form.get(i)

        if val is None or val == "":
            return f"Missing value for {i}"

        input_data.append(float(val))


    # Convert input into DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=columns
    )


    # Make prediction
    prediction = model.predict(input_df)


    # Show prediction on webpage
    return render_template(
        "index.html",
        prediction=round(float(prediction[0]), 2)
    )


# Run Flask
if __name__ == "__main__":
    app.run(debug=True)