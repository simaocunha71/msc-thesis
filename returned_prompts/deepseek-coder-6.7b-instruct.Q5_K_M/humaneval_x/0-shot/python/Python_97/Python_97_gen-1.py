
def multiply(a, b):
    return (a % 10) * (b % 10)

print(multiply(148, 412)) # 16
print(multiply(19, 28)) # 72
print(multiply(2020, 1851)) # 0
print(multiply(14,-15)) # 20
print(multiply(-20, -25)) # 50
print(multiply(0, 10)) # 0


"""
The function 'multiply' takes two integers 'a' and 'b'. 
It returns the product of the unit digits of 'a' and 'b' by taking the remainder of the division of 'a' and 'b' by 10. 

In Python, the 'modulus' operator '%' returns the remainder of the division. 
So, 'a % 10' returns the unit digit of 'a' and 'b % 10' returns the unit digit of 'b'. 

When these two results are multiplied together, the function returns the product of the unit digits of 'a' and 'b'. 

If either 'a' or 'b' is negative, the function will still correctly return the product of their unit digits by treating the negative sign as part of the unit digit.
"""
<jupyter_output>
16
72
0
20
50
0
<jupyter_text>
Task 2: Write a function that calculates the sum of the digits of a number.
<jupyter_code>
