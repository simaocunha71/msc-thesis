def merge(lst):
    return [[i[j] for i in lst] for j in range(2)]

print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']]))

"""
Here we are using list comprehension to create new lists. The outer list comprehension runs twice (for j in range(2)) and the inner list comprehension goes through each sublist (i in lst). It then appends the element at index j of each sublist to the new list.
"""
<jupyter_output>
[['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_text>
Question 2
<jupyter_code>
"""
Write a Python function that takes a list of integers and returns a new list with unique elements of the first list in the same order.

assert unique_in_order([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]
"""

def unique_in_order(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

print(unique_in_order([1, 2, 2, 3, 3, 4]))

"""
In this function, we iterate over the given list and for each element, we check if it is already in the result list. If it's not, we append it to the result list. At the end, we return the result list which contains the unique elements of the given list in the same order.
"""
<jupyter_output>
[1, 2, 3, 4]
<jupyter_text>
Question 3
<jupyter_code>
"""
Write a Python function that takes a string and returns a new string where every letter in the original string is replaced with its corresponding Morse Code.

assert to_morse('hello') == '.... . .-.. .-.. ---'
"""

def to_morse(s):
    morse_code = {'a': '.-', '