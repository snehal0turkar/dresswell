import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "supersecretkey"
    DATABASE_PATH = os.path.join(BASE_DIR, "instance", "dresswell.db")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    PREVIEW_FOLDER = os.path.join(BASE_DIR, "static", "previews")