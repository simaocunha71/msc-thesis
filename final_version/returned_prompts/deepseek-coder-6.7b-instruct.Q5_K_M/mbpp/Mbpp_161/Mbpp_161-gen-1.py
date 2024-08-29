
def remove_elements(list1, list2):
    return [i for i in list1 if i not in list2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# Output: [1, 3, 5, 7, 9, 10]

"""
Here, we are using list comprehension to iterate through each element in the list1 and if the element is not in list2 then we include it in the new list.
"""

"""
This solution has a time complexity of O(n^2) because for each element in list1 we are checking if it is in list2, which is an O(n) operation. Hence, the overall time complexity is O(n^2).
"""

"""
The space complexity is O(n) because we are storing the result in a new list.
"""

"""
A more efficient way would be to convert the lists to sets and use the difference method which has a time complexity of O(n).
"""

def remove_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# Output: [1, 3, 5, 7, 9, 10]

"""
This solution is more efficient because it avoids the need for nested loops and the time complexity is reduced to O(n).
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
