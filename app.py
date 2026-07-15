from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clv_secret_key"


# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # login credentials
        if username == "admin@gmail.com" and password == "admin123":

            session["user"] = username
            return redirect(url_for("dashboard"))

    return render_template("login.html")


# DASHBOARD PAGE
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    # if user not logged in
    if "user" not in session:
        return redirect(url_for("login"))

    prediction = None
    segment = None

    tenure = 24
    monthly = 60
    total = 1000
    satisfaction = 3

    if request.method == "POST":

        tenure = float(request.form["tenure"])
        monthly = float(request.form["monthly"])
        total = float(request.form["total"])
        satisfaction = float(request.form["satisfaction"])

        # CLV formula
        prediction = round((tenure * monthly * satisfaction) / 4 + (total * 0.3), 2)

        # segmentation
        if prediction < 2000:
            segment = "Low Value Customer"

        elif prediction < 5000:
            segment = "Medium Value Customer"

        else:
            segment = "High Value Customer"

    return render_template(
        "index.html",
        prediction=prediction,
        segment=segment,
        tenure=tenure,
        monthly=monthly,
        total=total,
        satisfaction=satisfaction
    )


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)