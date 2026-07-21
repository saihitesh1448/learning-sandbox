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