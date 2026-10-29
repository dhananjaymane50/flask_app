from flask import Flask, request, render_template
import pandas as pd
import joblib


obj = joblib.load("california.joblib")

model = obj["model"]
columns = obj["columns"]

app = Flask(__name__)


@app.route('/')
def Main():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():

    input_data = []

    for i in columns:

        val = request.form.get(i)

        if val is None or val =="":
            return f"Missing value for {i}"

        input_data.append(float(val))

    input_df = pd.DataFrame(
        [input_data],
        columns=columns
    )

    prediction = model.predict(input_df)

    return render_template(
        "index.html",
        prediction=round(float(prediction[0]), 2)
    
    )


if __name__ == "__main__":
    app.run(debug=True)