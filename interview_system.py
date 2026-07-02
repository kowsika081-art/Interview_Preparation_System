from question import Question
import random 

class InterviewSystem:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.correct = 0
        self.wrong = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_test(self):
        self.score = 0

        random.shuffle(self.questions)
        
        print("Total Questions:", len(self.questions))

        for question in self.questions:
            question.display_question()

            print("Enter only the option (A/B/C/D)")
            user_answer = input("Your Answer: ") 

            if user_answer.upper() == question.answer.upper():
                print("Correct Answer")
                self.score += 1
                self.correct += 1
            else:
                print("Wrong Answer")
                print("Correct Answer is:", question.answer)
                self.wrong += 1

    def display_score(self,name,department):

        if len(self.questions) == 0:
            print("No Questions Available")
            return

        percentage = (self.score / len(self.questions)) * 100
        print("\n===== Interview Report =====")
        print("Candidate Name  :", name)
        print("Department      :", department)
        print("Total Questions :", len(self.questions))
        print("Correct Answers :", self.correct)
        print("Wrong Answers   :", self.wrong)
        print("Score           :", self.score, "/", len(self.questions))
        print("Percentage      :", percentage, "%")

        if percentage >= 80:
            print("Result : Excellent")
        elif percentage >= 50:
            print("Result : Good")
        else:
            print("Result : Need Improvement")