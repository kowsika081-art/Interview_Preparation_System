Interview Preparation System (Python)

A simple console-based Interview Preparation System built using Python.
It helps users practice MCQ-based interview questions and calculates their score.

🚀 Features
Load questions from a text file
MCQ-based quiz system (A/B/C/D)
Category-wise questions (Python, Java, C, AIML)
Score calculation
Candidate name & department input
Simple console interface

🛠️ Technologies Used
Python 3
Object Oriented Programming (OOP)
File Handling
Loops & Conditional Statements

📂 Project Structure
Interview preparation system
│── main.py
│── question.py
│── load_questions.py
│── interview_system.py
│── interview_questions.txt

📄 Question File Format
Each question must follow this format:

Python
What is Python?
A. Language
B. Database
C. Browser
D. Operating System
A
---

▶️ How to Run
Open terminal in project folder
Run the program:
python main.py

🧑‍💻 How It Works
Questions are loaded from interview_questions.txt
User enters name and department
Quiz starts automatically
Score is calculated at the end

📊 Sample Output
===== Interview Report =====
Candidate Name  : kowsika
Department      : cse
Total Questions : 20
Correct Answers : 14
Wrong Answers   : 6
Score           : 14 / 20
Percentage      : 70.0 %
Result : Good

🎯 Future Improvements
GUI version (Tkinter)
Timer for each question
Score percentage display
Database storage
Login system

👩‍💻 Author

Kowsika.R
