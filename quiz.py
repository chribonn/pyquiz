# The Quiz and Question classes defined for a particular quiz
import datetime
import sys
import random

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0
        
    def print_header(self):
        print ("\n\n**********************************************")
        print (f"QUIZ NAME: {self.name}")
        print (f"DESCRIPTION: {self.description}")
        print (f"QUESTIONS: {len(self.questions)}")
        print (f"TOTAL POINTS: {self.total_points}")
        print ("**********************************************\n")
        
    def print_results(self, quiztaker, thefile = sys.stdout):
        print ("\n\n**********************************************", file=thefile, flush=True)
        print (f"Results for {quiztaker}", file=thefile, flush=True)
        print (f"Date: {datetime.datetime.today().strftime('%d/%m/%Y')}", file=thefile, flush=True)
        print (f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile, flush=True)
        print (f"SCORE: {self.score} points out of {self.total_points}", file=thefile, flush=True)
        print (f"PERCENTAGE: {self.score / self.total_points * 100:.2f}", file=thefile, flush=True)
        print (f"TIME TO COMPLETE: {self.completion_time}", file=thefile, flush=True)
        print ("**********************************************\n", file=thefile, flush=True)
 
    def take_quiz(self):
        # Initialise variables
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        
        for q in self.questions:
            q.is_correct = False
            self.total_points += q.points
            
        # Print the header
        self.print_header()
        
        # randomise the questions
        random.shuffle(self.questions)

        start_time = datetime.datetime.now()
        
        # Execute each question and record the result
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points
        print ("----------------------------------------------\n")
  
        end_time = datetime.datetime.now()
        
        if self.correct_count != len(self.questions):
            while True:
                response = input ("You did not get all the questions. Try failed questions? (y/n) ").lower()
                if response[0] == "y":
                    wrong_qs = [q for q in self.questions if q.is_correct == False]
                    for q in wrong_qs:
                        q.ask()
                        if (q.is_correct):
                            self.correct_count += 1
                            self.score += q.points
                    print ("----------------------------------------------\n")
                    end_time = datetime.datetime.now()
                    break
                elif response[0] == "n":
                    break
                else:
                    continue
        
        self.completion_time = end_time - start_time
        self.completion_time = datetime.timedelta(seconds = round(self.completion_time.total_seconds()))
        
        # Reutrn the results
        return (self.score, self.correct_count, self.total_points)


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

# MultiSelect class - there is more than one answer
class QuestionMS(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print (self.text)
            for a in self.answers:
                print (f"({a.name}) {a.text}")

            print ("Enter the correct answers seperated by commas")
            response = input("? ").lower()
            if len(response) == 0:
                self.InvalidInput()
                continue

            response = response.replace(" ", "")
            response_list = response.split(",")
            response_list.sort()

            # Validate input
            # Build the answer list
            ans_name_list = []
            for ans in self.answers:
                ans_name_list.append(ans.name)

            found = all(a in ans_name_list for a in response_list)
            if not found:
                self.InvalidInput()
                continue

            if self.correct_answer == response_list:
                self.is_correct = True

            break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

# if __name__ == "__main__":
#     qz = Quiz()
    
#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
    
#     qz.questions.append(q1)

#     q2 = QuestionMC()
#     q2.text = 'What is 2+2?'
#     q2.points = 10
#     q2.correct_answer = "b"

#     ans = Answer()
#     ans.name = "a"
#     ans.text = "3"
#     q2.answers.append(ans)

#     ans = Answer()
#     ans.name = "b"
#     ans.text = "4"
#     q2.answers.append(ans)

#     ans = Answer()
#     ans.name = "c"
#     ans.text = "5"
#     q2.answers.append(ans)

#     ans = Answer()
#     ans.name = "d"
#     ans.text = "6"
#     q2.answers.append(ans)
    
#     qz.questions.append(q2)

#     print (qz.take_quiz())

