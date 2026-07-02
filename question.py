class Question:
    def __init__(self, question_text, options, answer, category):
        self.question_text = question_text
        self.options = options
        self.answer = answer
        self.category = category

    def display_question(self):
        print("\nCategory:", self.category)
        print(self.question_text)

        for option in self.options:
            print(option)