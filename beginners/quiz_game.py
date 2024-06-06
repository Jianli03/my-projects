class Question:
  def __init__(self, question, answer, options=None):
    self.question = question
    self.answer = answer
    self.options = options

  def ask_question(self):
    if self.options:
      print(self.question)
      for i, option in enumerate(self.options):
        print(f"{i+1}. {option}")
      user_input = input("Enter your answer (number or full text): ")
      if isinstance(user_input, str) and user_input.lower() == self.answer.lower():
        return True
      elif user_input.isdigit() and int(user_input) - 1 == self.options.index(self.answer):
        return True
      else:
        return False
    else:
      user_input = input(self.question + " ")
      return user_input.lower() == self.answer.lower()

class ComputerQuiz:
  def __init__(self):
    self.questions = []
    self.score = 0

  def add_question(self, question, answer, options=None):
    self.questions.append(Question(question, answer, options))

  def play_game(self):
    print("Welcome to the Computer Quiz!")
    for question in self.questions:
      if question.ask_question():
        print("Correct!")
        self.score += 1
      else:
        print("Incorrect!")
    print(f"You got {self.score} questions correct out of {len(self.questions)}!")
    print(f"Your score is {(self.score / len(self.questions)) * 100:.2f}%")

if __name__ == "__main__":
  quiz = ComputerQuiz()
  quiz.add_question("What does CPU stand for?", "central processing unit")
  quiz.add_question("What does GPU stand for?", "graphics processing unit")
  quiz.add_question("What does RAM stand for?", "random access memory")
  quiz.add_question("What does PSU stand for?", "power supply")
  # You can add more questions here
  quiz.play_game()
  