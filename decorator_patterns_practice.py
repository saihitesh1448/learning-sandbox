def log_call(func):
    def inner(*args):
        return f"the function name is {func.__name__} and result is {func(*args)}"
    return inner

def validate_numbers(func):
    def inner(*args):
        for i in args:
            if isinstance(i,str):
                raise ValueError('string is plesent')
                break
        return func(*args)
    return inner
            

def handle_division_by_zero(func):
    def inner(*args):
        for i in args[1:]:
            if i==0:
                raise ZeroDivisionError
                break
        return func(*args)
    return inner

@validate_numbers
@log_call
def add(*args):
    return sum(args)

@validate_numbers
@log_call
def mul(*args):
    res=1
    for i in args:
        res*=i
    return res

@handle_division_by_zero
@validate_numbers
@log_call
def divided(*args):
    res=args[0]
    for i in args[1:]:
        res/=i
    return res
        

# ============================================
# AI TEST BLOCKS
# ============================================

# TEST 1: Normal case - add with valid numbers
print("TEST 1: Normal add(5, 3, 2)")
try:
    result = add(5, 3, 2)
    print(f"✅ PASS: {result}")
except Exception as e:
    print(f"❌ FAIL: {e}")

# TEST 2: Invalid input - string detection (should raise error)
print("\nTEST 2: Invalid input - add(5, '3') with string")
try:
    result = add(5, "3")
    print(f"❌ FAIL: Should have raised ValueError but got {result}")
except ValueError as e:
    print(f"✅ PASS: Caught expected error: {e}")

# TEST 3: Division by zero (should raise error)
print("\nTEST 3: Division by zero - divided(10, 0)")
try:
    result = divided(10, 0)
    print(f"❌ FAIL: Should have raised ZeroDivisionError but got {result}")
except ZeroDivisionError as e:
    print(f"✅ PASS: Caught expected error: {e}")

# TEST 4: Multiplication normal case
print("\nTEST 4: Normal mul(2, 3, 4)")
try:
    result = mul(2, 3, 4)
    print(f"✅ PASS: {result}")
except Exception as e:
    print(f"❌ FAIL: {e}")

# TEST 5: Edge case - single number in add
print("\nTEST 5: Edge case - add(5) single number")
try:
    result = add(5)
    print(f"✅ PASS: {result}")
except Exception as e:
    print(f"❌ FAIL: {e}")

# TEST 6: Division normal case
print("\nTEST 6: Normal divided(100, 2, 5)")
try:
    result = divided(100, 2, 5)
    print(f"✅ PASS: {result}")
except Exception as e:
    print(f"❌ FAIL: {e}")
