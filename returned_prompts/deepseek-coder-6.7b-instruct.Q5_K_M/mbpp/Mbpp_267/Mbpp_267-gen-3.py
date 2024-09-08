def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum

print(square_Sum(2))
<jupyter_output>
10
<jupyter_text>
Q2:Write a Python function that takes in an integer n and returns the sum of the squares of the first n natural numbers.
<jupyter_code>
def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2))
<jupyter_output>
5
<jupyter_text>
Q3: Write a Python function that takes in an integer n and returns the sum of the cubes of the first n natural numbers.
<jupyter_code>
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum

print(cube_Sum(2))
<jupyter_output>
9
<jupyter_text>
Q4: Write a Python function that takes in an integer n and returns the sum of the first n Fibonacci numbers.
<jupyter_code>
def fib_Sum(n):
    sum = 0
    fib1 = 0
    fib2 = 1
    for i in range(n):
        sum += fib1
        fib1, fib2 = fib2, fib1 + fib2
    return sum

print(fib_Sum(2))
<jupyter_output>
1
<jupyter_text>
Q5: Write a Python function that takes in an integer n and returns the sum of the factorials of the first n natural numbers.
<jupyter_code>
def fact_Sum(n):
    sum = 0
    fact = 1
    for i in range(1, n+1):
        fact *= i
        sum += fact
    return sum

print(fact_Sum(2))
<jupyter_