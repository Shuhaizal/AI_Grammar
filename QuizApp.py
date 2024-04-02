import streamlit as st
import random

class MathQuiz:
    def __init__(self, operation, num_questions=5, score=0):
        self.operation = operation
        self.num_questions = num_questions
        self.score = score

def generate_question(math_quiz):
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
        answer = num1 * num2  # Ensure a whole number division
        operator = '/'
        num1, num2 = answer, num2  # Swap to get the original numbers

    st.write(f"\nQuestion: {num1} {operator} {num2}")
    user_answer = st.text_input("Your Answer:")

    if user_answer.strip() == str(answer):
        st.write("Correct!")
        math_quiz.score += 1
    else:
        st.write(f"Wrong! The correct answer is: {answer}")

def take_quiz(math_quiz):
    for _ in range(math_quiz.num_questions):
        generate_question(math_quiz)

    st.write(f"\nQuiz Complete! Your Score: {math_quiz.score}/{math_quiz.num_questions}")

def main():
    st.title("Math Quiz Game")
    while True:
        choice = st.sidebar.selectbox("Select Operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

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

        another_action = st.sidebar.radio("Do you want to take another quiz?", ('Yes', 'No'))

        if another_action == 'No':
            st.write("Thank you for playing the Math Quiz Game!")
            break

if __name__ == "__main__":
    main()
