
def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10))) # 3

"""
Explanation:

In the given tuple, the first 3 elements are not tuples. So, the function counts them and returns 3.

Note: The function breaks the loop as soon as it finds a tuple. So it does not go through the entire tuple.
"""
<jupyter_output>
3
<jupyter_text>
