
def sum_common_divisors(n1, n2):
    common_divisors = []
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            common_divisors.append(i)
    return sum(common_divisors)

print(sum_common_divisors(10, 15))  # Output: 6

"""
Explanation:
In the function sum_common_divisors, we loop from 1 up to the minimum of n1 and n2. If n1 and n2 are divisible by i, we add i to common_divisors list. Finally, we return the sum of all numbers in common_divisors.
"""
<jupyter_output>
6
<jupyter_text>
Q2: Write a python function that takes a list of numbers and returns a dictionary where the keys are the numbers and the values are their squares.
<jupyter_code>
def squares(lst):
    return {num: num ** 2 for num in lst}

print(squares([1, 2, 3, 4, 5]))  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
<jupyter_output>
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
<jupyter_text>
Q3: Write a python function that takes a list of numbers and returns a list of squares of only those numbers which are divisible by 3.
<jupyter_code>
def squares_divisible_by_three(lst):
    return [num ** 2 for num in lst if num % 3 == 0]

print(squares_divisible_by_three([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [9, 36, 81]
<j