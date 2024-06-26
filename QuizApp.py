import streamlit as st
import random

class MathQuiz:
    def __init__(self, operation, num_questions=5, score=0):
        self.operation = operation
        self.num_questions = num_questions
        self.score = score
        self.questions = []

def generate_question(math_quiz):
    if not math_quiz.questions:
        for _ in range(math_quiz.num_questions):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            if math_quiz.operation == '1':  # Addition
                answer = num1 + num2
                operator = '+'
            elif math_quiz.operation == '2':  # Subtraction
                num1, num2 = max(num1, num2), min(num1, num2)  # Ensure a positive result
                answer = num1 - num2
                operator = '-'
            elif math_quiz.operation == '3':  # Multiplication
                answer = num1 * num2
                operator = '*'
            elif math_quiz.operation == '4':  # Division
                while num1 % num2 != 0:  # Ensure a whole number division
                    num1 = random.randint(1, 10)
                    num2 = random.randint(1, 10)
                answer = num1 // num2
                operator = '/'
                num1, num2 = answer, num2  # Swap to get the original numbers

            math_quiz.questions.append((num1, num2, operator, answer))

@st.cache(suppress_st_warning=True)
def take_quiz(math_quiz):
    math_quiz.score = 0
    generate_question(math_quiz)
    for i, (num1, num2, operator, answer) in enumerate(math_quiz.questions, 1):
        st.write(f"\nQuestion {i}: {num1} {operator} {num2}")
        user_answer = st.text_input(f"Your Answer for Question {i}:", key=f'user_answer_{math_quiz.operation}_{i}')

        if user_answer.strip():
            if user_answer.strip() == str(answer):
                st.write("Correct!")
                math_quiz.score += 1
            else:
                st.write(f"Wrong! The correct answer is: {answer}")

    st.write(f"\nQuiz Complete! Your Score: {math_quiz.score}/{math_quiz.num_questions}")

def main():
    st.title("Math Quiz Game")
    choice = st.sidebar.radio("Select Operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'], index=0)

    if choice == 'Addition':
        operation = '1'
    elif choice == 'Subtraction':
        operation = '2'
    elif choice == 'Multiplication':
        operation = '3'
    elif choice == 'Division':
        operation = '4'

    num_questions = st.sidebar.number_input("Enter the number of questions for the quiz:", min_value=1, value=5)
    math_quiz = MathQuiz(operation, num_questions)

    take_quiz(math_quiz)

if __name__ == "__main__":
    main()
