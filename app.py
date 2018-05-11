from flask import Flask, render_template, redirect, jsonify, request, url_for, flash, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

from data.articles import Articles
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "flask"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

articlesData = Articles()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html", articles = articlesData.getArticles())

@app.route("/article/<string:id>")
def article(id):
    return render_template("article.html", articleId = id)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Password do not match")
    ])
    confirm = PasswordField("Confirm Password")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate():

        name = request.form['name']
        username = request.form['username']
        email = request.form['password']
        password = sha256_crypt.encrypt(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, username, email, password) VALUES (%s, %s, %s, %s)", (name, username, email, password))

        mysql.connection.commit()

        cur.close()

        flash("You heve been registered", "success")

        redirect(url_for("home"))

    return render_template("register.html", form=form)

class LoginForm(Form):
    username = StringField('Username', [validators.input_required()])
    password = PasswordField('Password', [validators.input_required()])

@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm(request.form)

    if request.method == "POST":
        
        username = request.form["username"]
        formPassword = request.form["password"]

        print("formPassword", formPassword)

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT password FROM users WHERE username=%s", [username])
        
        if result > 0:
            userPassword = cur.fetchone()["password"]

            if sha256_crypt.verify(formPassword, userPassword):

                session["loggedIn"] = True
                session["username"] = username

                flash("You've been logged", "success")

                return redirect(url_for("dashboard"))

            else:
                flash("Incorect password", "danger")
            
            cur.close()

        else:
            flash("No user", "danger")
    
    return render_template("login.html", form=form)

def isLoggedIn(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "loggedIn" in session:
            return f(*args, **kwargs)
        else:
            flash("You are not loggin", "danger")
            return redirect(url_for("login"))
    return wrap

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for("about"))

@app.route("/dashboard")
@isLoggedIn
def dashboard():

    print(session["username"])

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", session["username"])
    userData = cur.fetchall()

    print(userData[0]["name"])

    return render_template("dashboard.html", userData = userData[0])

    cur.close()

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
    





























# if __name__ == '__main__':
#    app.run(debug = True)

# @app.route("/news")
# def news():
#     return jsonify(username="Tom", color="red")

# @app.route("/news/<int:news_id>")
# def newsId(news_id):
#     return 'News id is %d' % news_id

# @app.route("/add", methods=["POST", "GET"])
# def add():
#     error = ""
#     # error = None
#     senededValue = {
#         "val": request.form,
#         "name": "Tom",
#         "error": error
#     }
#     if request.method == "POST":
#         print(request.form["someName"])
#     else:
#         senededValue.error = 'Invalid value'
#     return render_template('hello.html', senededValue=request.form["someName"])