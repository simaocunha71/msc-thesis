
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += (2*i)**3
    return sum

print(cube_Sum(2))
<jupyter_output>
72
<jupyter_text>
Q2. Write a python program to find the cube sum of first n natural numbers.
<jupyter_code>
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum

print(cube_Sum(3))
<jupyter_output>
138
<jupyter_text>
Q3. Write a python program to compute the sum of digits in a given number.
<jupyter_code>
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

print(sum_of_digits(1234))  # 10
<jupyter_output>
10
<jupyter_text>
Q4. Write a Python program to check whether a number is perfect or not.
<jupyter_code>
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print(is_perfect(6))  # True
<jupyter_output>
True
<jupyter_text>
Q5. Write a Python program to generate all the perfect numbers in a given range.
<jupyter_code>
def perfect_numbers(start, end):
    perfects = []
    for i in range(start, end+1):
        if is_perfect(i):
            perfects.append(i)
    return perfects

print(perfect_numbers(1, 10000))
<jupyter_output>
[6, 