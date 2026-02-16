import json
import os

FILE_NAME = "questions.json"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_questions():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_questions(questions):
    with open(FILE_NAME, "w") as f:
        json.dump(questions, f, indent=4)

def add_question():
    print("\n--- Add New Question ---")

    question_text = input("Enter question: ")

    options = []
    for i in range(4):
        opt = input(f"Enter option {i+1}: ")
        options.append(opt)

    answer = input("Enter correct answer (must match exactly one option): ")

    if answer not in options:
        print("⚠ Error: Answer must match one of the options exactly.")
        return

    questions = load_questions()

    new_question = {
        "question": question_text,
        "options": options,
        "answer": answer
    }

    questions.append(new_question)
    save_questions(questions)

    print("✅ Question added successfully!")

def view_questions():
    questions = load_questions()

    if not questions:
        print("No questions found.")
        return

    print("\n--- All Questions ---")
    for idx, q in enumerate(questions, 1):
        print(f"\n{idx}. {q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"   {i}. {opt}")
        print(f"   ✔ Answer: {q['answer']}")

def delete_question():
    questions = load_questions()

    if not questions:
        print("No questions to delete.")
        return

    view_questions()
    try:
        choice = int(input("\nEnter question number to delete: "))
        if 1 <= choice <= len(questions):
            removed = questions.pop(choice - 1)
            save_questions(questions)
            print(f"✅ Deleted: {removed['question']}")
        else:
            print("Invalid question number.")
    except ValueError:
        print("Invalid input.")

def edit_question():
    questions = load_questions()

    if not questions:
        print("No questions to edit.")
        return

    view_questions()
    try:
        choice = int(input("\nEnter question number to edit: "))
        if not (1 <= choice <= len(questions)):
            print("Invalid question number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    q = questions[choice - 1]

    print("\nLeave blank to keep existing value.")

    new_question = input(f"Edit question [{q['question']}]: ")
    if new_question:
        q['question'] = new_question

    for i in range(4):
        new_option = input(f"Edit option {i+1} [{q['options'][i]}]: ")
        if new_option:
            q['options'][i] = new_option

    new_answer = input(f"Edit correct answer [{q['answer']}]: ")
    if new_answer:
        if new_answer in q['options']:
            q['answer'] = new_answer
        else:
            print("⚠ Answer must match one of the options. Edit cancelled.")
            return

    save_questions(questions)
    print("✅ Question updated successfully!")

def main():
    while True:
        print("\n===== Question Manager =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Edit Question")
        print("4. Delete Question")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            edit_question()
        elif choice == "4":
            delete_question()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
