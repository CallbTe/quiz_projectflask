from db.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS question (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        question    TEXT    NOT NULL,
        answer      TEXT    NOT NULL,
        wrong1      TEXT    NOT NULL,
        wrong2      TEXT    NOT NULL,
        wrong3      TEXT    NOT NULL,
        type        TEXT    NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_content (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id     INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        FOREIGN KEY (quiz_id)       REFERENCES quiz(id),
        FOREIGN KEY (question_id)   REFERENCES question(id)
    )
    """)

    conn.commit()
    conn.close()