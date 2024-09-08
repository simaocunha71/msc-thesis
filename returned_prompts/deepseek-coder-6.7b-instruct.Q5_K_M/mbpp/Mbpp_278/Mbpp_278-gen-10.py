
def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))

"""
Explanation:

The function count_first_elements takes a tuple as an argument.
It initializes a count variable to 0.
It then loops over each element in the tuple.
If the element is a tuple, it breaks out of the loop.
If the element is not a tuple, it increments the count.
Finally, it returns the count.
"""
<jupyter_output>
3
<jupyter_text>
