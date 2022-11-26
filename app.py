from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import Clothe
from PIL import Image
import os
from database import Clothe

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_post():
    files = request.files.getlist("file")
    for file in files:
        img = Image.open(file)
        img.save(os.path.join("static/images", file.filename))
    Clothe.create(file=files)
    # img.execute('INSERT INTO persons(n) values("Hanako")')
    return render_template("upload.html")



# @app.route('/create')
# def create():
#     return render_template("create.html")
# @app.route('/create', methods=["POST"])
# def method_name():
#     redirect()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
