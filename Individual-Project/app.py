from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import random
# import amogus


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
config = {
  "apiKey": "AIzaSyAMdHWBlh82MLximl6_8eex5NeP-dC-ucc",
  "authDomain": "netroulette0.firebaseapp.com",
  "projectId": "netroulette0",
  "storageBucket": "netroulette0.appspot.com",
  "messagingSenderId": "780923332394",
  "appId": "1:780923332394:web:a2b6ff385ad04b194aa053",
  "measurementId": "G-JEWN2T84LD",
  "databaseURL":"https://netroulette0-default-rtdb.europe-west1.firebasedatabase.app/"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()







@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"email": email, "password":password};
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            error = "Authentication failed"
    return render_template("signup.html")
# Your code should be below


@app.route("/")
def home():
    extention = ["net", ".com", ".co", ".biz", ".site", ".cc"];
    def spin():
        site = ""
        num = random.randint(1, 16)
        Letter = random.choice(string.ascii_letters)
        for i in range(num):
            site = site + Letter
        num = random.randint(0,6)
        site = site + (extention[num])

    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/site_of_the_week")
def site_of_the_week():
    return render_template("site_of_the_week.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
