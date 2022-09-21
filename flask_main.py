
from flask import Flask, render_template, request
import prediction as p
import random
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def prediction():
    pred = " "
    if request.method == "POST":
        myteam = int(request.form["team1"])
        apponent = int(request.form["team2"])
        venue = int(request.form["para1"])
        time = int(request.form["para2"])
        day = float(request.form["para3"])
        xg = float(request.form["para4"])
        xga = float(request.form["para5"])
        gf = float(request.form["para6"])
        if myteam == apponent:
            pred = 'ohh! Same team Name'
        elif myteam == 405 or apponent == 405 or venue == 405 or day == 405:
            pred = ' Choose Correct Option '
        elif time > 24 or time < 0:
            pred = 'Time Should be between 0 to 24'
        else:
            pred = (p.predict(venue, myteam, apponent, time, day, xg, xga, gf))

    return render_template("index.html", text=pred)


random.uniform(10.5, 75.5)

if __name__ == "__main__":
    app.run(debug=True)
