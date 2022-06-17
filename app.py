from crypt import methods
from flask import Flask, redirect, url_for, render_template, request
from rainwater import trap_rain_water
from rainwater import plot_rain_water
import random
import os

# initialize Flask application
app = Flask(__name__)

# landing page
@app.route("/")
def home():
    return render_template("home.html")

# this page is never directly accessed, it is embedded into trapping rain water page as IFrame
@app.route("/rain-water-model")
def rain_water_model():
    return render_template("rainwatermodel.html")


@app.route("/trapping-rain-water/", methods=['GET', 'POST'])
def trapping_rain_water():
    # randomly generate first time
    int_list = [random.randint(0, 10) for i in range(12)]
    
    temp = trap_rain_water(int_list)
    water = temp[0]
    trapped = temp[1]

    # all subsequent times, only randomly generate if client does not enter a list
    if request.method == 'POST':
        temp = request.form['list']

        if not temp:
            int_list = [random.randint(0, 10) for i in range(12)]
        else:
            # split user input into list of integers
            int_list = [int(x) for x in temp.split(',') if x.strip().isdigit()]

        temp = trap_rain_water(int_list)
        water = temp[0]
        trapped = temp[1]

    # generate Plotly model and export to HTML file
    plot_rain_water(int_list, trapped)
    
    # render template and pass in trapped water value
    return render_template("trappingrainwater.html", waterValue=water)


if __name__ == "__main__":
    # launch Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)