def remove_elements(lst1, lst2):
    for i in lst2:
        if i in lst1:
            lst1.remove(i)
    return lst1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
This code will remove all elements from the first list present in the second list.
It will return the first list after removing the elements present in the second list.
"""

"""
Alternatively, we can use list comprehension to solve this problem in a single line.
"""

def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
This list comprehension does the same thing as the previous code. It creates a new list that includes only the elements of lst1 that are not present in lst2.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 10]
[1, 3, 5, 7, 9, 10]
<jupyter_text>
11. Write a Python program to find the difference between two lists.
<jupyter_code>
def find_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(find_difference([1, 2, 3, 4, 5], [2, 4, 6, 8]))
<jupyter_output>
[1, 3, 5]
<jupyter_text>
12. Write a Python program to find common elements in three lists.
<jupyter_code>
def find_common_elements(lst1, lst2, lst3):
   