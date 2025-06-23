class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

    def is_correct(self, user_answer):
        return user_answer == self.answer
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0  
    def add_question(self, question):
        self.questions.append(question)  
    def start(self):
        self.score = 0
        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question.prompt}")
            for idx, choice in enumerate(question.choices, start=1):
                print(f"{idx}. {choice}")
            try:
                answer = int(input("Your answer (enter the option number): "))
                if question.is_correct(question.choices[answer - 1]):
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.answer}")
            except (ValueError, IndexError):
                print("Invalid choice! Moving to the next question.")
        print(f"\nQuiz finished! Your score is {self.score}/{len(self.questions)}")
quiz = Quiz()
question1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
quiz.add_question(question1)
quiz.start()