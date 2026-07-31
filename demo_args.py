def print_num(*args):
    print(*args)
    out=args
    print(type(out))

def sum_of_args(*args):
    s=0
    for i in args:
        s+=i
    return s

def sum_of_strings(*args):
    out=""
    for i in args:
       out+=i
    return out

def Normal_method(normal,*args):
    print(normal,end="    ")
    print(*args)

def loop(*args):
    for i in range(len(args)):
        print(f"{i+1} . {args[i]}")


assert sum_of_args(1,2,3,4,5) == 15, "Sum test failed"
print(" Test 1 passed: sum_of_args()")


assert sum_of_args() == 0, "Edge case test failed"
print("Test 2 passed: sum_of_args() with 0 arguments")

assert sum_of_strings("a","b","c") == "abc", "String sum test failed"
print(" Test 3 passed: sum_of_strings()")

assert sum_of_strings() == "", "String edge case test failed"
print(" Test 4 passed: sum_of_strings() with 0 arguments")

numbers = [5, 10, 15]
assert sum_of_args(*numbers) == 30, "Unpacking test failed"
print("Test 5 passed: Unpacking list with *")

try:
    sum_of_args("a", "b", "c")
    print(" Test 6 failed: Should have raised TypeError")
except TypeError:
    print(" Test 6 passed: Correctly caught TypeError for non-numeric input")
