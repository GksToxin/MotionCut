def get_questions():
    return [
        {
            "question": "Who is known as the 'Father of the Nation' in India?",
            "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Sardar Patel", "D. Dr. B.R. Ambedkar"],
            "answer": "B"
        },
        {
            "question": "Which city is the capital of India?",
            "options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Kolkata"],
            "answer": "C"
        },
        {
            "question": "Which is the national animal of India?",
            "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
            "answer": "B"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Lal Bahadur Shastri", "D. Indira Gandhi"],
            "answer": "B"
        },
        {
            "question": "Which river is known as the 'Ganga of the South'?",
            "options": ["A. Godavari", "B. Krishna", "C. Kaveri", "D. Yamuna"],
            "answer": "C"
        },
        {
            "question": "In which year did India gain independence from British rule?",
            "options": ["A. 1945", "B. 1946", "C. 1947", "D. 1948"],
            "answer": "C"
        },
        {
            "question": "Who wrote the national anthem of India?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhas Chandra Bose"],
            "answer": "A"
        }
    ]

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_user_answer():
    user_answer = input("Enter the correct option (A/B/C/D): ").upper()
    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return user_answer

def check_answer(question, user_answer):
    if user_answer == question["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {question['answer']}.")
        return False

def ask_questions(questions):
    score = 0
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if check_answer(question, user_answer):
            score += 1
        print()
    return score

def display_final_score(score, total_questions):
    print(f"Your final score is {score}/{total_questions}")

def main():
    questions = get_questions()

    print("Welcome to the Indian General Knowledge Quiz!")
    print("Answer the following questions by entering the correct option (A/B/C/D).\n")
    
    score = ask_questions(questions)
    display_final_score(score, len(questions))

if __name__ == "__main__":
    main()
