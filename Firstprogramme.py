class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def marks(self,n):
        self.l=[]
        print("please enter the student marks")
        for i in range(n):
            temp=int(input(f"enter subject {i+1} marks : "))
            self.l.append(temp)
        print(f"your marks{self.l}")
    def avg(self):
        self.avg=sum(self.l)/len(self.l)
        print(f"your average score is: {self.avg}")
    def is_passing(self):
        if self.avg>=40:
            print("you passed")
        else:
            print("you failed")
    def __str__(self):
        return (f"student name:{self.name} student ID:{self.id} ")
sai=Student("sai",123)
sai.marks(3)
sai.avg()
sai.is_passing()
print(sai)
        
    
        
