# QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        
        # Most recently selected quiz
        self.the_quiz = None
        
        # Collection of quizzes
        self.quizzes = dict()
        
        # Store result of most recent quiz
        self.results = None
        
        # Make sure that the quiz folder exists
        self.quiztaker = ""
        
        # Build the list of quizzes
        if (os.path.exists(self.quizfolder) == False):
            raise FileNotFoundError("The quiz folder does not seem to exist")
            
        
    def build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        for i, f in enumerate(dircontents):
            if f.is_file():
                root_ext = os.path.splitext(f)
                if root_ext[1] == ".xml":
                    parser = quizparser.QuizParser()
                    self.quizzes[i+1] = parser.parse_quiz(f)
                
        
    # Print a list of the current installed quizzes
    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print (f"({k}) {v.name}")
            
    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()
    
    # prints the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)
    
    # save the results ofthe most recent quiz to a file
    # the file is named using the current date as 
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        today = datetime.datetime.now()
        n = 1
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
        
        while (os.path.exists(filename)):
            n = n + 1
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            
        with open(filename, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)
        
    
    # if __name__ == "__main__":
    #     qm = QuizManager("Quizzes")
    #     qm.list_quizzes()
    