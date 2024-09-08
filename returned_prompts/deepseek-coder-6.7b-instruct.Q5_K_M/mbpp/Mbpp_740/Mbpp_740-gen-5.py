def tuple_to_dict(t):
    return {t[i]: t[i + 1] for i in range(0, len(t) - 1, 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

# Output: {1: 5, 7: 10, 13: 5}

"""
Explanation:
We use dictionary comprehension to create the dictionary. The key-value pairs are created by taking every two elements from the tuple. The for loop specifies that it should start at the first element (0), stop before the last (len(t) - 1), and step by two (2) elements at a time.
"""

"""
This solution assumes that the tuple always has an even number of elements. If this is not the case, we would need to add error checking to handle that situation.
"""
<jupyter_output>
{1: 5, 7: 10, 13: 5}
<jupyter_text>
Problem 3:
<jupyter_code>
