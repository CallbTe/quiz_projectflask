from db.connection import get_connection
from db.schema import create_tables
from scripts.seed import seed_questions, seed_quiz, seed_quiz_content
from db.query import get_questions_by_quiz_and_type, get_next_question
from web.app import create_app

app = create_app()
# def main():
#     current_id = 0
#     soal_ke = 0

#     while True:
#         q = get_next_question(last_id=current_id, quiz_id=1)
        
#         if not q:
#             print("\n=== Quiz Seleasi ===")
#             break

#         soal_ke += 1
#         current_id = q["id"]

#         print(f"\nsSoal {soal_ke}: {q['question']} [{q['type']}]")
#         print(f"    A.{q['answer']}")
#         print(f"    B.{q['wrong1']}")
#         print(f"    C.{q['wrong2']}")
#         print(f"    D.{q['wrong3']}")

#         input(" Tekan Enter untuk lanjut...")
    # questions = get_questions_by_quiz_and_type(1)
    # print(f"Semua soal Math Quiz: {len(questions)} soal")
    # for q in questions:
    #     print(" -", dict(q)['question'], f"[{dict(q)['type']}]")

    #     print()

    # easy = get_questions_by_quiz_and_type(1, 'easy')
    # print(f"Soal EASY Math Quiz: {len(easy)} soal")
    # for q in easy:
    #     print(" -", dict(q)['question'])
    # create_tables()
    # seed_questions()
    # seed_quiz()
    # seed_quiz_content()
    # print("Database seeded")
    #print("Tables created!")
    # conn = get_connection()
    # print("Database connected:", conn)
    # conn.close()

if __name__ == "__main__":
    app.run(debug=True)
    # main()