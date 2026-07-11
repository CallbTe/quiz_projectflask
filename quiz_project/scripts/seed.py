from db.connection import get_connection

def seed_questions():
    conn = get_connection()
    cursor = conn.cursor()

    questions = [
        #easy
        ("2+2=?", "4", "3", "5", "6", "easy"),
        ("3+5=?", "8", "7", "9", "10", "easy"),
        ("Ibukota RI?", "Jakarta", "Bandung", "Bali", "Medan", "easy"),
        #med
        ("12 x 12=?", "144", "124", "134", "154", "medium"),
        ("Planet terbesar?","Jupiter", "Mars", "Bumi", "Venus", "medium"),
        ("Air mendidih?", "100C", "90C", "80C", "70C", "medium"),
        #hard
        ("Integral x dx?", "x^2/2", "x", "2x", "x^3", "hard"),
        ("Teori relativitas?","Einstein","Newton","Tesla","Darwin","hard"),
        ("Binary 1010=?", "10", "12", "8", "15", "hard"),
    ]

    cursor.executemany("""
    INSERT INTO question (question, answer, wrong1, wrong2, wrong3, type)
    VALUES (?, ?, ?, ?, ?, ?)
    """, questions)

    conn.commit()
    conn.close()

def seed_quiz():
    conn = get_connection()
    cursor = conn.cursor()

    quizzes = [
        ("Math Quiz",),
        ("General Knowledge",)
    ]

    cursor.executemany("""
    INSERT INTO quiz (name)
    VALUES (?)
    """, quizzes)

    conn.commit()
    conn.close()

def seed_quiz_content():
    conn = get_connection()
    cursor = conn.cursor()

    links = [
        (1, 1),
        (1, 2),
        (1, 4),
        (1, 7),
        (1, 9),

        (2, 3),
        (2, 5),
        (2, 6),
        (2, 8)
    ]

    cursor.executemany("""
    INSERT INTO quiz_content (quiz_id, question_id)
    VALUES (?, ?)
    """, links)

    conn.commit()
    conn.close()