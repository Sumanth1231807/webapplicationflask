from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/contact')
def Contact():
    return render_template("contact.html")



@app.route('/home')
def home():
    return "welcome home"

@app.route('/gallery')
def gallery():
    return "welcome gallery"

if __name__ == "__main__":
    app.run()
