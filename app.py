from flask import Flask, render_template, url_for
from flask import request
import pickle
import numpy as np

model = pickle.load(open('uc.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def home():
    # Location = request.form['Location']
    # Year = request.form['Year']
    # Kilometers_Driven = request.form['Kilometers_Driven']
    # Fuel_Type = request.form['Fuel_Type']
    # Transmission = request.form['Transmission']
    # Owner_Type = request.form['Owner_Type']
    # Seats = request.form['Seats']
    # Company = request.form['Company']
    # Mileage = request.form['Mileage(km/kg)']
    # Engine = request.form['Engine(CC)']
    # Power = request.form['Power(bhp)']
    # print(float(Location) + float(Power))
    #arr = [[float(Location), float(Year), float(Kilometers_Driven), float(Fuel_Type), float(Transmission), float(Owner_Type), float(Seats), float(Company), float(Mileage), float(Engine), float(Power)]]
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(prediction)
    return render_template("index.html", prediction_text = "The Cost of the Car will be Rupees {} Lakhs".format(abs(float(prediction[0][0]))))
    
    


if __name__ == "__main__":
    app.run(debug=True)