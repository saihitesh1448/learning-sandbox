#ecommerce website
class ecommerce:
    discount=(30/100)
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

    def discount_rate(self):
        return self.discount
    def coupen(self,coupen_dis):
        global discount
        self.discount+=coupen_dis
        return self.discount
    def tax(self):
        def inner(x):
            return self.discount*x
        return inner



ob=ecommerce()
ob.profile()
n=int(input("enter the no of items:"))
l=[input(f"enter {i+1} item: ") for i in range(n)]
ob.cart(*l)
#--------AI Test Cases---------
print("=" * 50)
print("TEST 1: discount_rate() - read class attribute")
print("=" * 50)
result = ob.discount_rate()
assert result == 0.3
print(f"✓ Test 1 passed: discount_rate = {result}")
print()

print("=" * 50)
print("TEST 2: coupen() - modify discount")
print("=" * 50)
initial = ob.discount_rate()
new_discount = ob.coupen(0.1)
assert new_discount == 0.4
print(f"✓ Test 2 passed: discount increased from {initial} to {new_discount}")
print()

print("=" * 50)
print("TEST 3: tax() - closure returns inner function")
print("=" * 50)
tax_calculator = ob.tax()
result = tax_calculator(1000)
expected = 0.4 * 1000
assert result == expected
print(f"✓ Test 3 passed: tax on 1000 = {result}")
print()

print("=" * 50)
print("TEST 4: Multiple items in cart")
print("=" * 50)
result = ob.cart("item1", "item2", "item3")
assert len(result) == 3
print("✓ Test 4 passed: cart() works with multiple items")
print()

print("=" * 50)
print(" ALL TESTS PASSED!")
print("=" * 50)
    
    

