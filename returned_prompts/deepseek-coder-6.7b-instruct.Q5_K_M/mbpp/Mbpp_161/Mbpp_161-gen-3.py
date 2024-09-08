def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))  # Output: [1, 3, 5, 7, 9, 10]

"""
Explanation:
The function remove_elements takes two arguments: lst1 and lst2. 
It returns a new list which contains only those elements from lst1 that are not present in lst2. 
This is done using list comprehension, where for each element i in lst1, it checks if i is not in lst2. 
If the condition is satisfied, i is included in the new list.
"""

"""
Alternate Solution:

def remove_elements(lst1, lst2):
    for i in lst2:
        while i in lst1:
            lst1.remove(i)
    return lst1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))  # Output: [1, 3, 5, 7, 9, 10]
"""

"""
Explanation:
This alternate solution uses a nested loop. For each element i in lst2, it checks if i is in lst1. 
If it is, it removes i from lst1 using the remove() function. This continues until i is not found in lst1. 
Finally, it returns lst1. This solution is more time-consuming because it involves removing an element from lst1 in each iteration of the loop.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
