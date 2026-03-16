from flask import Flask, render_template
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Ensure required folders exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["PREVIEW_FOLDER"], exist_ok=True)
os.makedirs("instance", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)