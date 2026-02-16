import streamlit as st
import random
import json

st.set_page_config(page_title="Cyber Safety Quiz", page_icon="🔐")

st.title("🔐 Cyber Safety Awareness Quiz")
st.write("Test your knowledge about online safety!")

# Load questions from external JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

if len(questions) == 0:
    st.error("No questions found in questions.json!")
    st.stop()

# Initialize session state
MAX_QUESTIONS = 5  # Number of questions per quiz session

if "shuffled_questions" not in st.session_state:
    total_available = len(questions)

    if total_available <= MAX_QUESTIONS:
        st.session_state.shuffled_questions = random.sample(questions, total_available)
    else:
        st.session_state.shuffled_questions = random.sample(questions, MAX_QUESTIONS)

    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.finished = False
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.finished = False

if not st.session_state.finished:

    q_data = st.session_state.shuffled_questions[st.session_state.current_question]

    st.subheader(f"Question {st.session_state.current_question + 1}")
    st.write(q_data["question"])

    selected_option = st.radio(
        "Choose your answer:",
        q_data["options"],
        key=f"question_{st.session_state.current_question}"
    )

    # Track if answer was submitted
    if "answered" not in st.session_state:
        st.session_state.answered = False

    if not st.session_state.answered:
        if st.button("Submit Answer"):
            if selected_option == q_data["answer"]:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! ❌ Correct answer: {q_data['answer']}")

            st.session_state.answered = True

    else:
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.session_state.answered = False

            if st.session_state.current_question >= len(st.session_state.shuffled_questions):
                st.session_state.finished = True

            st.rerun()

else:
    total = len(st.session_state.shuffled_questions)
    score = st.session_state.score
    percentage = (score / total) * 100

    st.header("🎉 Quiz Completed!")
    st.write(f"Your Score: **{score}/{total}**")
    st.write(f"Percentage: **{percentage:.2f}%**")

    if percentage == 100:
        st.success("Excellent! You are Cyber Smart 🔐🔥")
    elif percentage >= 50:
        st.info("Good job! You know basic cyber safety.")
    else:
        st.warning("You need more awareness. Stay safe online!")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
