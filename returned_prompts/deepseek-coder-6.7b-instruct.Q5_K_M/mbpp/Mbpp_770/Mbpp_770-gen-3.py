def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum

print(odd_num_sum(2))
<jupyter_output>
82
<jupyter_text>
Q2: Write a python function to find the sum of cubes of first n natural numbers.
<jupyter_code>
def sum_of_cubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum

print(sum_of_cubes(3))
<jupyter_output>
36
<jupyter_text>
Q3: Write a python function to find the sum of squares of first n natural numbers.
<jupyter_code>
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(sum_of_squares(3))
<jupyter_output>
14
<jupyter_text>
Q4: Write a python function to find the sum of square of first n even natural numbers.
<jupyter_code>
def sum_of_even_squares(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**2
    return sum

print(sum_of_even_squares(3))
<jupyter_output>
56
<jupyter_text>
Q5: Write a python function to find the sum of square of first n odd natural numbers.
<jupyter_code>
def sum_of_odd_squares(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum

print(sum_of_odd_squares(3))
<jupyter_output>
91
<jupyter_text>
Q