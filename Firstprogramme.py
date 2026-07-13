class Student:
    def __init__(self):
        self.name="Not Entered"
        self.id="Not Entered"
        self.l=[]
        self.avgerage=0.0
    def details(self):
        self.name=input("enter the name : ")
        self.id=input("enter the id : ")
    def print_details(self):
        print(f"Student name: {self.name}    student ID: {self.id}")
    def marks(self,n):
        self.l=[]
        print("please enter the student marks")
        for i in range(n):
            while True:
                temp=int(input(f"enter subject {i+1} marks : "))
                if 0<=temp<=100:
                    self.l.append(temp)
                    break
                else:
                    print("Invalid marks! Please enter a value between 0 and 100.")
        print(f"your marks{self.l}")
    def avg(self):
        if len(self.l)==0:
            print("No marks have been entered yet. Average score is: 0.0")
            return
        self.avg=sum(self.l)/len(self.l)
        print(f"your average score is: {self.avg}")
    def is_passing(self):
        if self.avg>=40:
            print("you passed")
        else:
            print("you failed")
    def __str__(self):
        return (f"student name:{self.name} student ID:{self.id} ")

students = []          # list of Student objects
current = None         # the student currently being worked on

while True:
    print("menu:")
    print("1.add new student\n2.enter marks\n3.student details\n4.list all students\n5.highest scorer\n6.exit")
    op = int(input("enter the option: "))
    match op:
        case 1:
            current = Student()
            current.details()
            students.append(current)
            print("student added successfully!")

        case 2:
            if current is None:
                print("please add a student first (option 1)")
            else:
                n = int(input("enter how many subjects the student is studying: "))
                current.marks(n)

        case 3:
            if current is None:
                print("no student selected yet")
            else:
                current.print_details()
                current.avg()
                current.is_passing()

        case 4:
            if not students:
                print("no students added yet")
            else:
                print("----- all students -----")
                for s in students:
                    print(s)   # uses __str__

        case 5:
            if not students:
                print("no students added yet")
            else:
                topper = max(students, key=lambda s: s.average)
                print(f"highest scorer: {topper.name} (ID: {topper.id}) with average {topper.average}")

        case 6:
            print("......you are exiting.......")
            break

        case _:
            print("please select valid option")
