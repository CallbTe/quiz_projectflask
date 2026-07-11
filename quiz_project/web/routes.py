from db.query import get_all_quizzes, get_next_question
from flask import redirect, url_for, session

def register_routes(app):
    
    @app.route('/')
    def home():
        quizzes = get_all_quizzes()
    
        html = "<h1>Quiz List</h1><ul>"

        for q in quizzes:
            html += f"<li><a href='/start/{q['id']}'>{q['name']}</a></li>"

        html += "</ul>"
        return html
    
    @app.route("/start/<int:quiz_id>")
    def start_quiz(quiz_id):
        session["quiz_id"] = quiz_id
        session["last_id"] = 0

        return redirect(url_for("question"))

    @app.route("/question")
    def question():
        quiz_id = session.get("quiz_id")
        last_id = session.get("last_id", 0)

        if not quiz_id:
            return "<h2>Belum pilih quiz. <a href='/'>Kembali</a></h2>"

        q = get_next_question(last_id, quiz_id)

        if not q:
            return "<h2>Quiz selesai! <a href='/'>Main lagi</a></h2>"
        
        session['last_id'] = q["id"]

        html = f"""
        <h2>{q['question']}</h2>
        <ul>
            <li>{q['answer']}</li>
            <li>{q['wrong1']}</li>
            <li>{q['wrong2']}</li>
            <li>{q['wrong3']}</li>
        </ul>
        <a href='/question'>Next</a>
        """

        return html