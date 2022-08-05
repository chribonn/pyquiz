# pyquiz.py -- Main starting point of the program

from quizmanager import QuizManager

class QuizApp:
    QUIZ_FOLDER = "Quizzes"
    
    def __init__(self):
        self.username =  ""
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)
        self.qm.build_quiz_list()

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
            selection = input("Enter your selection ").upper()

            if len(selection) == 0:
                self.menu_error()
                continue
            elif selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print ("These are the available quizes")
                self.qm.list_quizzes()

                # TODO: Show the quizes
                print ("-------------------------------\n")
            elif selection[0] == "T":
                try:
                    quiznum = int(input("Enter quiz number:"))
                    print ("You have selected {0}".format(quiznum))

                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                except:
                    self.menu_error()
                    
                # offer to save the results
                while True:
                    saveresults = input("Save the results? (y/n): ")
                    if len(saveresults) == 0:
                        continue
                    
                    saveresults = saveresults.capitalize()
                    if saveresults[0] == "Y":
                        self.qm.save_results()
                        break
                    elif saveresults[0] == "N":
                        break
                    else:
                        continue
                     
                # show the menu again
                self.menu_header()
            elif selection[0] == "E":
                self.goodbye()
                break
            else:
                self.menu_error()

    # This is the entry point to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program meny and run until the user exists
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()





