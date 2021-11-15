from flask import Flask, render_template,request,redirect,flash

user=[]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register",methods=["POST"])
def register_user():
    email = request.form.get("mail")
    password = request.form.get("firstpassword")
    # user.append([email,password])
    # print(user)
    return render_template("loginSuccess.html",value="registered",mail=email)

@app.route("/loginSuccess", methods=["POST"])
def loginSuccess():
    email = request.form.get('mail')
    password = request.form.get('password')
    return render_template("loginSuccess.html",value="logged",mail=email)
    # for i in user:
    #     if i[0]==email and i[1]==password:
    #         return render_template("loginSuccess.html",mail=email,password=password)
    # return "invalid credientials" 
    

if __name__ == "__main__":
    app.run(debug=True)

