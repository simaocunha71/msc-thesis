
def is_sublist(larger, smaller):
    return [i for i in range(len(larger)) if larger[i:i+len(smaller)] == smaller]

print(is_sublist([2,4,3,5,7],[3,7]))

# Output: []
# This means the function returns an empty list, which indicates that the smaller list is not found in the larger list.

"""
In the given problem, we are given two lists, larger and smaller. We need to check if smaller list is present in the larger list or not. 
We can do this by using list slicing method in python. We iterate over the larger list and for each element, we slice the larger list from that element to the length of the smaller list. 
If the sliced list is equal to the smaller list, then it means smaller list is present in the larger list at that position so we return True. 
If we don't find the smaller list in the larger list, we return False.
"""

# Time complexity: O(n*m)
# Space complexity: O(n)

"""
Here, 'n' is the size of the larger list and 'm' is the size of the smaller list. The reason behind the time complexity of O(n*m) is because in the worst case scenario, we are iterating over the larger list 'n' times and for each iteration, we are slicing the larger list 'm' times.
The space complexity is O(n) because in the worst case scenario, we may need to store all elements of the larger list in the list comprehension.
"""

# Note:
# This solution will return the starting indices of the smaller list in the larger list if it is present. If the smaller list is not found in the larger list, it will return an empty list.
# If you want to return True or False, you can modify the function to return True if the list is not empty and False if the list is empty.
<jupyter_output>
[]
<jupyter_text>
Question 2:
<jupyter_code>
