
def otherside_rightangle(base, height):
    return (base**2 + height**2)**0.5

print(otherside_rightangle(7,8))
<jupyter_output>
10.63014581273465
<jupyter_text>
4.Write a Python function to solve the quadratic equation.
<jupyter_code>
def solve_quadratic(a, b, c):
    import math
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

print(solve_quadratic(1, -3, 2))
<jupyter_output>
(3.0, 1.0)
<jupyter_text>
5.Write a Python function to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_text>
6.Write a Python function to check if a number is even or odd.
<jupyter_code>
def even_or_odd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(even_or_odd(7))
<jupyter_output>
Odd
<jupyter_text>
7.Write a Python function to find the sum of all even numbers in a list.
<jupyter_code>
def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
<jupyter