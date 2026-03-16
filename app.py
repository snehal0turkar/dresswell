from flask import Flask, render_template, request, redirect
from config import Config
import sqlite3
import os
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config.from_object(Config)

# Ensure required folders exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["PREVIEW_FOLDER"], exist_ok=True)
os.makedirs("instance", exist_ok=True)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Registration Route
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        conn = sqlite3.connect("instance/dresswell.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)