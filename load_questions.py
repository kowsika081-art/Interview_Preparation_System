from question import Question

def load_questions(filename):
    questions = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            blocks = file.read().strip().split("---")

            for block in blocks:
                lines = [line.strip() for line in block.strip().split("\n") if line.strip()]

                if len(lines) < 7:
                    continue

                category = lines[0]
                question = lines[1]
                option1 = lines[2]
                option2 = lines[3]
                option3 = lines[4]
                option4 = lines[5]
                answer = lines[6]

                q = Question(
                    question,
                    [option1, option2, option3, option4],
                    answer,
                    category
                )

                questions.append(q)

    except FileNotFoundError:
        print("Error: File not found!")

    return questions