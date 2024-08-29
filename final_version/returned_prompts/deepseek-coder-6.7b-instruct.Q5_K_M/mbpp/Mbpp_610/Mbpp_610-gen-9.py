def remove_kth_element(lst, k):
    return lst[:k] + lst[k+1:]

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

"""
Here, we are using python's slicing to get the elements before the k'th index and after the k'th index and concatenating them.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)
<jupyter_output>
[1, 1, 3, 4, 4, 5, 1]
<jupyter_text>
Question 2
<jupyter_code>
