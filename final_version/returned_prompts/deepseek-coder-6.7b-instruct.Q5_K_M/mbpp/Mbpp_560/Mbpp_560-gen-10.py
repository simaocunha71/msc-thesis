def union_elements(t1, t2):
    union = t1 + t2
    return tuple(sorted(union))

print(union_elements((3, 4, 5, 6), (5, 7, 4, 10)))

# Output: (3, 4, 5, 6, 7, 10)

"""
The function `union_elements` takes two tuples as arguments. It first concatenates these tuples to get all the elements together. 
Then, it uses the built-in `sorted` function to sort the elements. The sorted elements are then returned as a tuple.
"""

# You can also use set to solve this problem in a simpler way
def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))

print(union_elements((3, 4, 5, 6), (5, 7, 4, 10)))

# Output: (3, 4, 5, 6, 7, 10)
"""
The `set` function is used to remove duplicate elements from the concatenated tuple. Then, the sorted function is used to sort the elements, and the result is returned as a tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 11
<jupyter_code>
