from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my wedsite"

@app.route('/contact')
def Contact_page():
    return "contact page"

@app.route('/home')
def home():
    return "welcome home"

@app.route('/gallery')
def gallery():
    return "welcome gallery" \
           ""
if __name__ == "__main__":
    app.run()
