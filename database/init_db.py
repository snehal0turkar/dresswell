import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "dresswell.db")

os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# CLOTHING ITEMS
cursor.execute("""
CREATE TABLE IF NOT EXISTS clothing_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    category TEXT,
    image_path TEXT,
    color_rgb TEXT,
    color_hsv TEXT,
    occasions TEXT,
    temp_min INTEGER,
    temp_max INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# OUTFIT FEEDBACK
cursor.execute("""
CREATE TABLE IF NOT EXISTS outfit_feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    item_ids TEXT,
    feedback_type TEXT,
    harmony_type TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# SAVED OUTFITS
cursor.execute("""
CREATE TABLE IF NOT EXISTS saved_outfits (
    outfit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    items TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database initialized successfully!")