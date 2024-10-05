

    if len(l) == 0:
        return True
    else:
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))

print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))


# This solution works by checking if all the elements in the list are either monotonically increasing or decreasing.
# It does this by iterating through the list and comparing each pair of elements.
# If any pair of elements is not in order, the function returns False.
# If the function has iterated through the entire list without finding any out of order pairs, it returns True.
<jupyter_output>
True
False
True
<jupyter_text>
**Problem 4:**Write a function called `same_num_chars` that takes two strings as arguments and returns `True` if the strings have the same number of characters and `False` otherwise.
<jupyter_code>
