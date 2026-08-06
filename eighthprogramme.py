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
        for i in args:
            print(f"product name: {i}")
        return args

    def calculate_total(self, *prices):
        return sum(prices)

    def discount_rate(self):
        return self.discount
    
    def coupen(self,coupen_dis):
        self.discount+=coupen_dis
        return self.discount
    
    def tax(self):
        def inner(x):
            return self.discount*x
        return inner
    
    def update_info(self, **info):
        print(info)
        print("please check the info you entered if you want edit please enter 1")
        op=int(input())
        if op==1:
            name=input("enter the name of product:")
            if_want=bool(input("if want enter the True if dont want enter False: "))
            product={name:if_want}
            info.update(product)
            print(info)
            return info
        else:
            return "you exited........"





#---------------AI Test Blocks------------------
ob=ecommerce()
ob.profile()
n=int(input("enter the no of items:"))
l=[input(f"enter {i+1} item: ") for i in range(n)]
ob.cart(*l)

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
print("TEST 4: calculate_total() - bulk price calculator with *args")
print("=" * 50)
result = ob.calculate_total(100, 200, 300, 150)
assert result == 750
print(f"✓ Test 4 passed: calculate_total = {result}")
print()

print("=" * 50)
print("TEST 5: calculate_total() - edge case (0 arguments)")
print("=" * 50)
result = ob.calculate_total()
assert result == 0
print(f"✓ Test 5 passed: calculate_total with 0 arguments = {result}")
print()

print("=" * 50)
print("TEST 6: calculate_total() - single price")
print("=" * 50)
result = ob.calculate_total(500)
assert result == 500
print(f"✓ Test 6 passed: calculate_total with single price = {result}")
print()

print("=" * 50)
print("ALL TESTS PASSED!")
print("=" * 50)
