def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
This program uses list comprehension to create a new list that includes only the elements of lst1 that are not in lst2.
The 'in' operator is used to check if an element is in lst2. 
"""

#Testing
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([1, 1, 1, 2, 2, 2], [1, 2]) == []
assert remove_elements([1, 2, 3, 4, 5], []) == [1, 2, 3, 4, 5]
assert remove_elements([], [1, 2, 3]) == []
assert remove_elements(['a', 'b', 'c'], ['a', 'b']) == ['c']
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
