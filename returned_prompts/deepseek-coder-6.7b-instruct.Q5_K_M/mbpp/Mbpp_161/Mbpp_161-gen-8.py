def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# Alternative solution using list comprehension and the built-in function set()

def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in set(lst2)]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# Alternative solution using built-in function set() and the "difference" method

def remove_elements(lst1, lst2):
    return list(set(lst1).difference(set(lst2)))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
Note:
The time complexity for this problem is O(n^2) because we are iterating over the first list and for each element we are checking if it's in the second list.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 10]
[1, 3, 5, 7, 9, 10]
[1, 3, 5, 7, 9, 10]
<jupyter_text>
3. Write a function to find the intersection of two lists.
<jupyter_code>
