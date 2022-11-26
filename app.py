from flask import Flask
from flask import render_template
import cv2
import sys

# from database import Clothe

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/')
def create():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('camera', frame)
        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
# @app.route('/create')
# def create():
#     return render_template("create.html")


# @app.route('/create', methods=["POST"])
# def method_name():
#     redirect()


if __name__ == "__main__":
    app.run(debug=True)
