from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def display(self):
        return f"Name:{self.name} Empid: {self.empid}"
    @abstractmethod
    def calculate_salary(self):
        pass
        

class FullTimeEmp(Employee):
    def __init__(self,name,empid):
         super().__init__(name,empid)
         self.__base_salary="Not Entred"
    def display(self):
        info=super().display()
        return f"{info}  Type: Full Time Employee"
    @property
    def base_salary(self):
        return self.__base_salary
    @base_salary.setter
    def base_salary(self,n):
        if  n<0 :
            raise ValueError("salary must contain positive nums")
        self.__base_salary=n
    def calculate_salary(self):
        self.base_salary=int(input("enter the formula  "))
        self.fullsalary=self.base_salary+5000
        return f"the full time employee salary is: {self.fullsalary}"
    

class PartTimeEmp(Employee):
    def __init__(self,name,empid):
        super().__init__(name,empid)
        self.__base_salary="Not Entred"
    def display(self):
        info=super().display()
        return f"{info}  Type: Part Time Employee"
    @property
    def base_salary(self):
        return self.__base_salary
    @base_salary.setter
    def base_salary(self,n):
        if  n<0:
            raise ValueError("salary must contain positive nums")
        self.__base_salary=n
    def calculate_salary(self):
        self.base_salary=int(input("enter the base salary: "))
        self.fullsalary=self.base_salary+1000
        return f"the part time employee salary is: {self.fullsalary}"
    

class Manager(FullTimeEmp):
    def __init__(self,name,empid):
        super().__init__(name,empid)
    def display(self):
        info=super().display()
        return f"{info}  Type: Manager"
    def calculate_salary(self):
        super().calculate_salary()   
        self.fullsalary+=10000
        return f"the manager salary is: {self.fullsalary}"

class Taxable:
    def calculate_tax(self):
        return f"your tax is : {self.base_salary * 0.1}"

class SeniorBenefits:
    def calculate_tax(self):
        return f"your benifit is: {self.base_salary * 0.05}"

class SeniorManager(Manager, Taxable, SeniorBenefits):  
    pass 

class PayRoll:
    def __init__(self):
        self.employes=[]
    def add_employee(self,employee):
        self.employes.append(employee)
    def show_all(self):
        for i in self.employes:
            print(i.display())
            print(i.calculate_salary())
            if hasattr(i, "calculate_tax"):     
                print(i.calculate_tax())
            print("-----------------------------------------")


# ---- test block ----
 
# individual class tests
ft = FullTimeEmp("Bob", "F1")
ft.base_salary = 30000
print(ft.display())
print(ft.calculate_salary())
print("=====")
 
pt = PartTimeEmp("Sam", "P1")
pt.base_salary = 15000
print(pt.display())
print(pt.calculate_salary())
print("=====")
 
mgr = Manager("Alice", "M1")
mgr.base_salary = 40000
print(mgr.display())
print(mgr.calculate_salary())
print("=====")
 
sm = SeniorManager("Priya", "SM1")
sm.base_salary = 60000
print(sm.display())
print(sm.calculate_salary())
print(sm.calculate_tax())
print("=====")
 
# check abstract class is blocked
try:
    Employee("X", "E1")
except TypeError as e:
    print("Employee() blocked as expected:", e)
 
# check negative salary is blocked
try:
    ft.base_salary = -500
except ValueError as e:
    print("Negative salary blocked as expected:", e)
 
# check MRO
print(SeniorManager.__mro__)
 
# full payroll test
payroll = PayRoll()
payroll.add_employee(FullTimeEmp("Bob", "F1"))
payroll.employes[0].base_salary = 30000
payroll.add_employee(PartTimeEmp("Sam", "P1"))
payroll.employes[1].base_salary = 15000
payroll.add_employee(Manager("Alice", "M1"))
payroll.employes[2].base_salary = 40000
payroll.add_employee(SeniorManager("Priya", "SM1"))
payroll.employes[3].base_salary = 60000
 
payroll.show_all()
 


