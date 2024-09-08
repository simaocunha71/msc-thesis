
def check_distinct(tup):
    return len(tup) == len(set(tup))

print(check_distinct((1, 4, 5, 6, 1, 4)))

#output: False

"""
Explanation:
The function check_distinct uses the built-in set() function, which removes duplicate elements from a given iterable. The length of the tuple is compared with the length of the set of the tuple. If lengths are equal, it means that the tuple contains no duplicates. If lengths are not equal, it means that the tuple contains duplicates.
"""
<jupyter_output>
False
<jupyter_text>
