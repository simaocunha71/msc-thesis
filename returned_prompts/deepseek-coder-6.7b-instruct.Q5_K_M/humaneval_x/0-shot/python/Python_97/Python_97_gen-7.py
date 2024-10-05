
def multiply(a, b):
    return (abs(a)%10)*(abs(b)%10)

# Test cases
print(multiply(148, 412))  # should return 16
print(multiply(19, 28))  # should return 72
print(multiply(2020, 1851))  # should return 0
print(multiply(14,-15))  # should return 20
<jupyter_output>
16
72
0
20
<jupyter_text>
Q2:Write a Python function that takes in a list of integers and returns a list of only the even integers.
<jupyter_code>
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Test cases
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # should return [2, 4, 6, 8, 10]
print(even_numbers([100, 200, 300, 400, 500]))  # should return [100, 200, 300, 400, 500]
print(even_numbers([1, 3, 5, 7, 9]))  # should return []
<jupyter_output>
[2, 4, 6, 8, 10]
[100, 200, 300, 400, 500]
[]
<jupyter_text>
Q3:Write a Python function that takes in a list of integers and returns a dictionary with the following structure:{mean: , median: , mode: , range: }
<jupyter_code>
from collections import Counter
import statistics

def calculate_stats(lst):
    mean = statistics.mean(lst)
    median = statistics.median