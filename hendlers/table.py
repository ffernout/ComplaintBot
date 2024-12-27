from aiogram import Router, types
from aiogram.fsm.state import StatesGroup, State
import sqlite3

desktop_router = Router()

class Questions(StatesGroup):
    name = State()
    contact = State()
    extra_comments = State()

def complaints():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    contact TEXT
    extra_comments TEXT
)
''')

    conn.commit()
    conn.close()


complaints()

def save_complaints(name, contact, extra_comments):
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()

    cursor.execute('''
INSERT INTO complaints (name, contact, extra_comments) VALUES (?, ?, ?);
                   ''', (name, contact, extra_comments))

    conn.commit()
    conn.close()