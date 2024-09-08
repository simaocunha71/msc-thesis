def multiply_int(a, b):
    return a * b

print(multiply_int(10, 20))

# OR

def multiply_int(a, b):
    return a * b

assert multiply_int(10, 20) == 200

# OR

def multiply_int(a, b):
    return a * b

result = multiply_int(10, 20)
print(result)

# OR

def multiply_int(a: int, b: int) -> int:
    return a * b

assert multiply_int(10, 20) == 200

# OR

def multiply_int(a: int, b: int) -> int:
    result = a * b
    return result

assert multiply_int(10, 20) == 200

# OR

def multiply_int(a: int, b: int) -> int:
    result = a * b
    print(result)

multiply_int(10, 20)

# OR

def multiply_int(a: int, b: int) -> int:
    result = a * b
    return result

result = multiply_int(10, 20)
print(result)
<jupyter_output>
200
200
<jupyter_text>
2.Write a function that adds two numbers
<jupyter_code>
def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(10, 20)
print(result)
<jupyter_output>
30
<jupyter_text>
3.Write a function that subtracts two numbers
<jupyter_code>
def subtract_two_numbers(a, b):
    return a - b

result = subtract_two_numbers(20, 10)
print(result)
<jupyter_output>
1