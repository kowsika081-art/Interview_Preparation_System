from question import Question
from interview_system import InterviewSystem
from load_questions import load_questions
import os

system = InterviewSystem()


questions = load_questions("interview_questions.txt")

print("Total Questions Loaded:", len(questions))

for question in questions:
    system.add_question(question)

name = input("Enter your name: ")
department = input("Enter your department: ")

print("\n-----Candidate Details -----")
print("Name:", name)
print("Department:", department)

system.start_test()
system.display_score(name, department)