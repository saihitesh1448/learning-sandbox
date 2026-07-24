class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        return f"Brand : {self.brand} Model : {self.model} Year : {self.year}"
    def move(self):
        print("moving.....")
    def honk(self):
        print("treeeen....treeeen....treeeen...")
class Car(Vehicle):
    def __init__(self,brand,model,year,no_doors):
        super().__init__(brand,model,year)
        self.no_doors=no_doors
    def display(self):
        basicinfo=super().display()
        return f"Info: {basicinfo}  Number of doors:{self.no_doors}"
    def move(self):
        print("movoing on the road")
    
class Electric(Car):
    def __init__(self,brand,model,year,no_doors,battery_cap):
        super().__init__(brand,model,year,no_doors)
        self.battery_cap=battery_cap
    def display(self):
        basicinfo=super().display()
        return f"Info: {basicinfo}  Battery capacity : {self.battery_cap}"
    def move(self):
        print("silently moving")
class Boat(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
    def display(self):
        return super().display()
    def move(self):
        print("moving on water")
class Airplane(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
    def display(self):
        return super().display()
    def move(self):
        print("flies on air")
class Engine:
    def start_engine(self):
        print("engine is starting....")
class ElectricSystem(Engine):
    def start_engine(self):
        print("engine is engaging.....")
class Hybrid(Engine):
    def start_engine(self):
        print("Hybrid engine is starting....")
class HybridVehicle(ElectricSystem,Hybrid):
    pass


class Fleet:
    def __init__(self):
        self.vehicles = []          

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)   

    def show_all(self):
        for v in self.vehicles:         
            print(v.display())  
            v.move()                    
            print("-----")


fleet = Fleet()

fleet.add_vehicle(Car("Toyota", "Corolla", 2022, 4))
fleet.add_vehicle(Electric("Tesla", "Model 3", 2023, 4, 75))
fleet.add_vehicle(Boat("SeaRay", "Sundancer", 2021))
fleet.add_vehicle(Airplane("Boeing", "737", 2020))

fleet.show_all()




        


    
        
    
    
