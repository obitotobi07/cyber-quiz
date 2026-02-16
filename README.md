# 🔐 Cyber Safety Awareness Quiz App

## 📌 Project Overview

The **Cyber Safety Awareness Quiz App** is a Python-based web application developed using Streamlit.
It promotes cyber security awareness through an interactive quiz system.

The project follows modular architecture:

* Quiz Application Layer (Streamlit)
* Data Storage Layer (JSON)
* Question Management System (Terminal-based CRUD tool)

The system dynamically selects a limited number of questions per session to ensure fairness and variability.

---

## 🎯 Objective

To educate students about:

* Strong password practices
* OTP security
* Phishing attacks
* Safe browsing habits
* Digital payment safety in India

---

## 🛠 Technologies Used

* Python 3
* Streamlit
* JSON (Data Storage)
* File Handling
* Random Module
* Session State Management

---

## 📂 Project Structure

```
cyber_quiz_project/
│
├── cyber_quiz_app.py      # Main Streamlit Quiz Application
├── question_manager.py    # Terminal-based CRUD Manager
├── questions.json         # Stores quiz data
├── README.md              # Documentation
└── requirements.txt       # Requirements 
```

---

## ⚙ Features

### 🎮 Quiz Application

* Interactive Web Interface
* Randomized Question Selection
* Limited to 5 Questions Per Session
* Score & Percentage Calculation
* Session State Tracking

### 🛠 Question Management System

* Add Question
* View Questions
* Edit Question
* Delete Question
* JSON-based Persistent Storage

---

## 🧠 Technical Implementation

* Questions are stored externally in `questions.json`.
* The `question_manager.py` provides full CRUD operations.
* The quiz dynamically selects 5 random questions using Python’s `random.sample()` function.
* Session state maintains quiz progress.
* The system ensures fairness by randomizing questions every session.

---

## 🧩 System Design Principle

This project follows:

* Modular Programming
* Separation of Concerns
* Scalable Architecture
* Data Persistence using JSON
* Dynamic Question Sampling

---

# 🚀 Installation & Execution Guide

## 📦 1️⃣ Clone or Download the Project

```bash
git clone <repository-link>
cd cyber_quiz_project
```

Or manually download and extract the folder.

---

## 🐍 2️⃣ Create Virtual Environment (Recommended)

### On Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

This isolates project dependencies.

---

## 📥 3️⃣ Install Required Dependencies

Then run:

```bash
pip install -r requirements.txt
```


## 🛠 4️⃣ Run Question Manager (Optional)

To Add / Edit / Delete questions:

```bash
python3 question_manager.py
```

This will open the terminal-based CRUD manager.

---

## 🌐 5️⃣ Run the Quiz Application

```bash
streamlit run cyber_quiz_app.py
```

The application will automatically open in your default web browser.

If not, open the URL shown in the terminal (usually):

```
http://localhost:8501
```

---

## 🔄 Restarting the Quiz

Click the **Restart Quiz** button inside the app
OR
Stop the server using:

```
CTRL + C
```

Then run the Streamlit command again.

---

## 👨‍💻 Developed By

P. Lalitha Sri (under guidance)
Class IX – Computer Subject Project for Subject Fair

---
