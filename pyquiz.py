# Example file for "Build a Quiz"
# pyquiz.py -- Main starting point of the program

class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting at startup
        self.greeting()

        self.username = input("What is your name? ")
        print (f"Welcome {self.username}!")
        print ()

    def greeting(self):
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("~~~~~~~~~~~~~ Welcome to PyQuiz! ~~~~~~~~~~~~~")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ()

    def menu_header(self):
        print ("------------------------------")
        print ("Please make a selection:")
        print ("(M): Repeat this menu")
        print ("(L): List quizzes")
        print ("(T): Take a quiz")
        print ("(E): Exit")

    def menu_error(self):
        print ("That's not a valid selection. Please try again.")

    def goodbye(self):
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (f"Thanks for using PyQuiz, {self.username}!")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def menu(self):
        self.menu_header()

        # run until the user exists the app
        while True:
            selection = input ("Enter your selection").upper()

            if selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print ("These are the available quizes")

                # TODO: Show the quizes
                print ("-------------------------------\n")
                continue
            elif selection[0] == "T":
                try:
                    quiznum = int(input("Enter quiz number:"))
                    print ("You have selected {0}".format(quiznum))

                    # TODO: Start the quiz
                except:
                    self.menu_error()

                # TODO: Load and run the quiz
                continue
            elif selection[0] == "E":
                self.goodbye()
                break
            else:
                self.menu_error()
                continue

    # This is the entry point to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program meny and run until the user exists
        self.menu()






