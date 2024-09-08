
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))

"""
In this function, we are iterating through the given tuple. If we encounter a tuple element, we stop the iteration and return the count. Otherwise, we increment the count by 1.
"""
<jupyter_output>
3
<jupyter_text>
Problem 4:
<jupyter_code>
