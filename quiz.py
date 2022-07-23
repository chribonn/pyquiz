# The Quiz and Question classes defined for a particular quiz
import quiz


class Question:
    def __init__(self):
        self.text = ""
        self.points = 0
        self.correct_answer = ""
        self.is_correct = False

    def InvalidInput(self) -> None:
        print ("Your input is not valid. Please try again.")

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print (f"(T)rue or (F)alse: {self.text}")
            response = input("? ").lower()

            if len(response) == 0:
                self.InvalidInput()
                continue
            elif response[0] != "t" and response[0] != "f":
                self.InvalidInput()
                continue
            elif response[0] == self.correct_answer:
                self.is_correct = True

            break

class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print (self.text)
            for a in self.answers:
                print (f"({a.name}) {a.text}")

            response = input("? ").lower()
            if len(response) == 0:
                self.InvalidInput()
                continue

            found = False
            for a in self.answers:
                if a.name == response[0]:
                    found = True
                    break

            # Check that the input is one of the valid answers
            if not found:
                self.InvalidInput()
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True

            break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

if __name__ == "__main__":
    q1 = QuestionTF()
    q1.text = "Broccoli is good for you"
    q1.points = 5
    q1.correct_answer = "t"
    q1.ask()

    q2 = QuestionMC()
    q2.text = 'What is 2+2?'
    q2.points = 10
    q2.correct_answer = "b"

    ans = Answer()
    ans.name = "a"
    ans.text = "3"
    q2.answers.append(ans)

    ans = Answer()
    ans.name = "b"
    ans.text = "4"
    q2.answers.append(ans)

    ans = Answer()
    ans.name = "c"
    ans.text = "5"
    q2.answers.append(ans)

    ans = Answer()
    ans.name = "d"
    ans.text = "6"
    q2.answers.append(ans)

    q2.ask()

    print (q1.is_correct)
    print (q2.is_correct)
