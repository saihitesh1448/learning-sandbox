from staticmethod_demo import BillUtils
class Bill:
    def __init__(self,person,money):
        self.person=person
        self.money=money
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,n):
        if not isinstance(n, (int, float)):
            raise ValueError("money must be a number")
        if n < 0:
            raise ValueError("money cannot be negative")
        self.__money = n
    def __str__(self):
        return f"Name: {self.person}  Money :{self.money} rupees"
    
    def __eq__(self,other):
        return self.money==other.money

    def __lt__(self,other):
        return self.money<other.money
        
    def __gt__(self,other):
        return self.money>other.money
    def __add__(self, other):
        return self.money+other.money
    def __repr__(self):
        return f"Bill(person={self.person}, money={self.money})"

class BillSplitter:
    def __init__(self):
        self.peoples=[]
    def add_people(self,person, money_paid):
        if BillUtils.is_valid(money_paid):
            self.peoples.append(Bill(person, money_paid))
        else:
            raise ValueError("invalid money")
    def show_all(self):
        for i in self.peoples:
            print(i)
    @property
    def total_bill(self):
        total=0
        for i in self.peoples:
            total+=i.money
        return total
    def splitter(self):
        indi = BillUtils.split_bill(self.total_bill, len(self.peoples))   # call the property itself
        return f"every one should pay {indi}"
    def __len__(self):
        return len(self.peoples)
    def __contains__(self, name):
        for i in self.peoples:
            if i.person==name:
                return True
        else:
            return False
    @classmethod
    def create_sample(cls):
        ob=cls()
        ob.add_people("rahul",100)
        ob.add_people("priya",800)
        ob.add_people("krithi",1000)
        return ob

splitter = BillSplitter()
splitter.add_people("sai", 200)
splitter.add_people("rahul", 500)

print("Manual splitter:")
print("Total bill:", splitter.total_bill)
print("Number of people:", len(splitter))
print("Is 'sai' in splitter?", "sai" in splitter)

print("\nSample splitter (created via @classmethod):")
sample = BillSplitter.create_sample()
print("Total bill:", sample.total_bill)
print("Number of people:", len(sample))
print("Per-person share:", sample.splitter())
    
