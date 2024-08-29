def similar_elements(a, b):
    return [i for i in a if i in b]

print(set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))))

"""
Output:
{4, 5}
"""

# Explanation:
# The function `similar_elements` iterates over the first list `a` and checks if each element is in the second list `b`. If the element is in `b`, it is added to the output list. The function then returns this list. The set is used to remove duplicates from the output.
<jupyter_output>
{4, 5}
<jupyter_text>
2. Write a Python program to remove all duplicates words from a given sentence.
<jupyter_code>
