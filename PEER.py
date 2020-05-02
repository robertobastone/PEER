################################################### PEER

author = 'Roberto Bastone'
version = 1.01

################################################### IMPORT
from termcolor import colored
import PEERsReal as real

class PEERs:
    yes = {'Y','y','YES','yes','Yes'}
    no = {'N','n','NO','no','No'}
    #### INITIALIZING
    def __init__(self):
        print colored("Initializing... Pythonic Easy Equation Resolvers version " + str(version), 'blue')
        print colored("(Author: " + author+')', 'blue')
    #### INITIALIZING        
    def main(self):
        self.introduction(self.yes,self.no)    
        self.solverChoice()
    ### INTRODUCTION
    def introduction(self,yes,no):
        while True:
            choice = raw_input(">PEERs can solve different kind of equations. Do you want me to print a list of the available commands? [y/n] \n").lower()
            if choice in yes:
                print ">1) By typing \"real\", PEERs will solve equations in 1 variable in the set of real numbers;"
                print ">2) Typing \"quit\" will terminate the execution of the script;"
                break
            elif choice in no:
                print">Okay, let us continue"
                break
            else:
                print( colored(">Please, select [y/n] only",'yellow'))
                continue
    ### SOLVERs CHOICE
    def solverChoice(self):
        while True:
            fnct = raw_input(">What solver do you choose? ").lower()
            if ( fnct == "real"):
                solver = real.PEERsReal()
                solver.main()  
                self.keepOnSolving(self.yes,self.no)
                break
            elif( fnct == "quit"):
                self.sayingGoodbye()
                break
            else:
                print( colored('>Error! Type a valide entry','red'))
                continue
    ### KEEP ON SOLVING?
    def keepOnSolving(self, yes, no):
        while True:
            choice = raw_input(">Do you want to rerun PEERs? [y/n] \n").lower()
            if choice in yes:
                self.solverChoice()
                break
            elif choice in no:
                self.sayingGoodbye()
                break
            else:
                print( colored(">Please, select [y/n] only",'yellow'))
                continue
    ### SAYING GOODBYE
    def sayingGoodbye(self):
        print colored("Terminating... Pythonic Easy Equation Resolvers version " + str(version),'blue')
