def func1():
    x=99
    print(x)
func1()

y=20
def func2():
    print(y)

func2()

def func():
    global y
    y+=1

func()
print(y)

def func3():
    y+=1

def func4():
    z=200
    def func5():
        print(z+1)
    func5()
    print(z)

func4()

def func6():
    a=90
    def func7():
        nonlocal a
        a+=10
    func7()
    print(a)

func6()

def len(x):
    return "custom len"

print(len([1,2,3,4]))

# ===== (AI) TEST BLOCKS =====

# Test 1: Global variable - read and modify
print("=" * 50)
print("TEST 1: Global variable read and modify")
print("=" * 50)
global_counter = 10

def increment_global():
    global global_counter
    global_counter += 5

increment_global()
assert global_counter == 15, "Global should be 15"
print(f"✓ Test 1 passed: global_counter = {global_counter}")
print()

# Test 2: Local variable - can't access outside
print("=" * 50)
print("TEST 2: Local variable scope")
print("=" * 50)
def test_local():
    local_num = 50
    return local_num

result = test_local()
assert result == 50, "Should return local variable"
print(f"✓ Test 2 passed: Local variable = {result}")
print()

# Test 3: Enclosing scope - inner reads outer
print("=" * 50)
print("TEST 3: Enclosing scope")
print("=" * 50)
def outer():
    outer_val = 100
    def inner():
        return outer_val + 10
    return inner()

result = outer()
assert result == 110, "Should access enclosing scope"
print(f"✓ Test 3 passed: Enclosing scope = {result}")
print()

# Test 4: Nonlocal - modify enclosing variable
print("=" * 50)
print("TEST 4: Nonlocal keyword")
print("=" * 50)
def outer2():
    value = 20
    def inner():
        nonlocal value
        value += 30
    inner()
    return value

result = outer2()
assert result == 50, "Nonlocal should modify"
print(f"✓ Test 4 passed: Nonlocal modified = {result}")
print()

# Test 5: Shadowing - local hides global
print("=" * 50)
print("TEST 5: Variable shadowing")
print("=" * 50)
shadow_val = "global"

def shadow_func():
    shadow_val = "local"
    return shadow_val

result = shadow_func()
assert result == "local", "Should return local"
assert shadow_val == "global", "Global should be unchanged"
print(f"✓ Test 5 passed: Local shadows global")
print()

print("=" * 50)
print("✅ ALL TESTS PASSED!")
print("=" * 50)