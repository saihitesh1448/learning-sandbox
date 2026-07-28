class BillUtils:
    @staticmethod
    def is_valid(amount):
        return isinstance(amount, (int, float)) and amount >= 0
    @staticmethod
    def split_bill(total,no_people):
        if no_people<=0:
            raise ValueError("enter the valid value")
        return (total//no_people)
    
    
