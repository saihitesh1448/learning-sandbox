#ecommerce website
class ecommerce:
    def profile(self,**kwargs):
        kwargs["name"]=input("enter the name:")
        kwargs["phone_no"]=input("enter the phone number:")
        kwargs["DOB"]=input("enter the date of birth: ")
        kwargs["state"]=input("enter the state:")
        kwargs["city"]=input("enter the city or colony name:")
        return kwargs

    
    def cart(self, *args):
        print(f"Items: {args}")
        return args

ob=ecommerce()
ob.profile()
n=int(input("enter the no of items:"))
l=[input(f"enter {i+1} item: ") for i in range(n)]
ob.cart(*l)
