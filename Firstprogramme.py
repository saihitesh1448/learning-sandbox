class Student:
    def __init__(self):
        self.name="Not Entered"
        self.id="Not Entered"
        self.l=[]
        self.avg=0.0
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

ob=Student()

while True:
    print("menue:")
    print("1.student name\n2.enter marks\n3.your dteails 4.exit")
    op=int(input("enetr the option:"))
    match(op):
        case 1:
            ob.details()
        case 2:
            n=int(input("enter how many subjects the student is studying: "))
            ob.marks(n)
        case 3:
            ob.print_details()
            ob.avg()
            ob.is_passing()
        case 4:
            print("......you are exiting.......")
            break
        case _:
            print("please select valid option")
