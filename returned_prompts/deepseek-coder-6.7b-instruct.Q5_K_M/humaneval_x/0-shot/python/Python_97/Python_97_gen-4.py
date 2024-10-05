
def multiply(a, b):
    a = str(a)
    b = str(b)
    a = a[-1]
    b = b[-1]
    return int(a) * int(b)

print(multiply(148, 412))  # should return 16
print(multiply(19, 28))  # should return 72
print(multiply(2020, 1851))  # should return 0
print(multiply(14,-15))  # should return 20



"""
Alternative solution:

def multiply(a, b):
    return (a % 10) * (b % 10)
"""
<jupyter_output>
16
72
0
20
<jupyter_text>
Solution explanation: The function takes two integers as inputs. We convert these integers to strings and then take the last digit of each string (the unit digit) by indexing at -1. Finally, we convert these digits back to integers and return the product.  Task 3: Write a Python function that takes a list of integers and returns the difference between the largest and smallest values.Example: difference([10, 20, 30, 40, 50]) should return 40 (50 - 10 = 40)
<jupyter_code>
