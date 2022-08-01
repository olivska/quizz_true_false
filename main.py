from question_model import Question
from data import question_data
from quizz_brain import QuizzBrain

question_bank = []
for element in question_data:
    question = Question(element["text"], element["answer"])
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_question():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quizz.score}/{len(question_bank)}")
