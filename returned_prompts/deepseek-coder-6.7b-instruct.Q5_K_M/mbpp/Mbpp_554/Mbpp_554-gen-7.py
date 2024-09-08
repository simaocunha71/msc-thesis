def Split(lst):
    return [i for i in lst if i%2 != 0]

print(Split([1,2,3,4,5,6]))

"""
This program works by using a list comprehension to iterate over each item in the given list. If the item is not divisible by 2 (i.e., it is odd), it is added to the new list. The result is a list of all odd numbers in the original list.
"""
<jupyter_output>
[1, 3, 5]
<jupyter_text>
2. Write a Python function to count the number of even numbers in a list.
<jupyter_code>
def count_even(lst):
    return len([i for i in lst if i%2 == 0])

print(count_even([1,2,3,4,5,6]))
<jupyter_output>
3
<jupyter_text>
3. Write a Python function that takes a list of strings and returns a new list with the strings sorted by their length.
<jupyter_code>
def sort_strings(lst):
    return sorted(lst, key=len)

print(sort_strings(["apple", "banana", "cherry", "date"]))
<jupyter_output>
['date', 'cherry', 'apple', 'banana']
<jupyter_text>
4. Write a Python function that takes a list of integers and returns the sum of the squares of all the integers.
<jupyter_code>
def sum_squares(lst):
    return sum([i**2 for i in lst])

print(sum_squares([1,2,3,4,5]))
<jupyter_output>
55
<jupyter_text>
5. Write a Python function that takes a list of integers and returns the product of the integers.
<jupyter_code>
def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(product([1,2,