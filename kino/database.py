import sqlite3
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEED_DB_PATH = os.path.join(BASE_DIR, "kino_bot.db")
DB_PATH = os.getenv("DB_PATH", SEED_DB_PATH)

# Render disk birinchi marta bo'sh bo'lsa, repodagi kino katalogini unga ko'chiramiz.
if os.path.abspath(DB_PATH) != os.path.abspath(SEED_DB_PATH):
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    if not os.path.exists(DB_PATH) and os.path.exists(SEED_DB_PATH):
        shutil.copy2(SEED_DB_PATH, DB_PATH)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Baza va jadvallarni yaratish"""
    conn = get_db()
    cursor = conn.cursor()

    # Foydalanuvchilar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Kinolar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            code INTEGER PRIMARY KEY,
            file_id TEXT NOT NULL,
            file_type TEXT DEFAULT 'video',
            caption TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# Foydalanuvchi qo'shish
def add_user(user_id: int, username: str, first_name: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username, first_name) 
        VALUES (?, ?, ?)
    """, (user_id, username, first_name))
    conn.commit()
    conn.close()


# Foydalanuvchilar soni
def get_users_count() -> int:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count


# Barcha foydalanuvchilar (xabar tarqatish uchun)
def get_all_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = [row['user_id'] for row in cursor.fetchall()]
    conn.close()
    return users


# Kino qo'shish
def add_movie(code: int, file_id: str, file_type: str = 'video', caption: str = "") -> bool:
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO movies (code, file_id, file_type, caption) 
            VALUES (?, ?, ?, ?)
        """, (code, file_id, file_type, caption))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Xatolik: {e}")
        return False


# Kino qidirish (kod orqali)
def get_movie(code: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT code, file_id, file_type, caption FROM movies WHERE code = ?", (code,))
    movie = cursor.fetchone()
    conn.close()
    return movie


# Kino o'chirish
def delete_movie(code: int) -> bool:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE code = ?", (code,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted


# Kinolar soni
def get_movies_count() -> int:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]
    conn.close()
    return count
