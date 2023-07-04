from Question import Question

question_prompts= [
    "What color is ant?\n(a)blue\n(b)black\n(c)red\n\n",
    "What color is apple?\n(a)blue\n(b)black\n(c)red\n\n",
    "What color is sky?\n(a)blue\n(b)black\n(c)red\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)