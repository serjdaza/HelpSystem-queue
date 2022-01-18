from collections import deque

class Student:
    def __init__(self) -> None:
        self.name = "Unnamed"
        self.course = "Unkonown"

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        
        print ("Now helping {1} with {0}".format(self.course, self.name))

class HelpSystem:

    def __init__(self) -> None:
        #super().__init__()
        self.waiting_list = deque()

    def is_student_waiting(self):
        if len(self.waiting_list) >= 1:
            return True
        else:
            return False

    def add_to_waiting_list(self, Student):
        self.waiting_list.append(Student)

    def help_next_student(self):
        if self.is_student_waiting() == True:
            # How can this work if display() function is not defined in this class? And there is no inheritance either
            # This line prints the Student at the head of the queue using the display() method from Student() class and pop it from the deque
            self.waiting_list.popleft().display()
        else:
            print ("No one to help")

def options_show():
    print ("Options:")
    print ("1. Add a new student")
    print ("2. Help next student")
    print ("3. Quit")

def main():
    help_sys = HelpSystem()
    # Variable status controls the while loop
    status = True
    # Option stores the selection from user
    option = ""
    
    while status:
        options_show()
        option = input ("Enter selection: ")

        if option == "1":
            print ("")
            new_student = Student()
            new_student.prompt()
            help_sys.add_to_waiting_list(new_student)
            print ("")

        elif option == "2":
            print ("")
            help_sys.help_next_student()
            print ("")

        elif option == "3":
            print("\nGoodbye")
            status = False

if __name__ == "__main__":
    main()