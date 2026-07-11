from db.connection import get_connection

def get_questions_by_quiz(quiz_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN question q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
    ORDER BY qc.id
    """, (quiz_id,))

    results = cursor.fetchall()
    conn.close()
    return results

def get_questions_by_quiz_and_type(quiz_id, q_type=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN question q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
    """
    params = [quiz_id]

    if q_type:
        query += " AND q.type = ?"
        params.append(q_type)

    query += " ORDER BY qc.id"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def get_next_question(last_id=0, quiz_id=1, q_type=None):
    """
    last_id = 0
    last_id = 3
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT qc.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3, q.type
    FROM quiz_content qc
    JOIN question q ON qc.question_id = q.id
    WHERE qc.quiz_id = ?
        AND qc.id > ?
    """
    params = [quiz_id, last_id]

    if q_type:
        query += " AND q.type = ?"
        params.append(q_type)

    query += " ORDER BY qc.id LIMIT 1"

    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close
    return result

def get_all_quizzes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM quiz")
    results = cursor.fetchall()

    conn.close()
    return results