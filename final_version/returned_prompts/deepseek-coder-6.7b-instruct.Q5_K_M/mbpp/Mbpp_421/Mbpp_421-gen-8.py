def concatenate_tuple(tup):
    return '-'.join(map(str, tup))

print(concatenate_tuple(("ID", "is", 4, "UTS")))

# Output: ID-is-4-UTS

"""
Explanation:
Here, we are given a tuple of elements. We are required to concatenate the elements of this tuple by the delimiter "-". The `map` function is used to convert every element to string because the `join` function only works with string. The `join` function is then used to join all the elements of the tuple by the delimiter "-".
"""
<jupyter_output>
ID-is-4-UTS
<jupyter_text>
Question 2
<jupyter_code>
