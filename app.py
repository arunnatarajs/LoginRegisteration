from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>HELLO Arun !<p>"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/loginSuccess", methods=["POST"])
def loginSuccess():
    email = request.form.get('mail')
    return render_template("loginSuccess.html",mail=email) 
    

if __name__ == "__main__":
    app.run(debug=True)

