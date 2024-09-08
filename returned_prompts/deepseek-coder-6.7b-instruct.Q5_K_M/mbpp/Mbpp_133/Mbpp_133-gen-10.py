def sum_negativenum(lst):
    sum = 0
    for num in lst:
        if num < 0:
            sum += num
    return sum

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

"""
Output:
-32
"""

# Alternatively, you can use list comprehension to solve the problem in a more concise way:

def sum_negativenum(lst):
    return sum([num for num in lst if num < 0])

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

"""
Output:
-32
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5:Write a Python function to return the number of occurrences of the number 10 in a given list of numbers.For example, if the list is [10, 20, 30, 10, 40, 50, 10], the function should return 3.
<jupyter_code>
def count_occurrences(lst):
    return lst.count(10)

print(count_occurrences([10, 20, 30, 10, 40, 50, 10]))
<jupyter_output>
3
<jupyter_text>
Question 6:Write a Python function that takes a list of numbers and returns the product of all the numbers in the list.
<jupyter_code>
def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

print(product([2, 3, 4, 5]))
<jupyter_output>
120
<jupyter_text>
Question 7:Write a Python function that takes a list of numbers and returns a new list with all the