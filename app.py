import os

from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import Clothe
from PIL import Image
import os
from database import Clothe
from database import Type
from database import User

app = Flask(__name__)


@app.route("/index")
# @login_required
def index():
    files = Clothe.select()  # .where(Clothe.name == User.name).get()
    return render_template("index.html", files=files)


@app.route("/")
def upload():
    types = Type.select()
    return render_template("upload.html", types=types)


@app.route("/upload", methods=["POST"])
def upload_post():
    # print("types")
    # print(types)
    files = request.files.getlist("file")
    for file in files:
        # img = Image.open(file)
        file_name = str(file.filename)
        file_path = "static/images/" + file_name
        file.save(os.path.join("static/images/", file_name))
        # img.save(os.path.join("static/images", file.filename))
        type = request.form['type']
        Clothe.create(file=file_path, type=type)
    # img.execute('INSERT INTO persons(n) values("Hanako")')
    return render_template("upload.html")


from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from database import User


app.config["SECRET_KEY"] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    name = request.form["name"]
    password = request.form["password"]
    user = User.get(name=name)
    if check_password_hash(user.password, password):
        login_user(user)
        return redirect("/")
    return redirect("/login")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signup', methods=["POST"])
def register():
    name = request.form["name"]
    password = request.form["password"]
    User.create(
        name=name,
        password=generate_password_hash(password, method="sha256"))
    # User.create(name=name, password=password)
    return redirect("/login")


# from flask_login import logout_user
@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect("/login")

# @app.route('/create')
# def create():
#     return render_template("create.html")
# @app.route('/create', methods=["POST"])
# def method_name():
#     redirect()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
