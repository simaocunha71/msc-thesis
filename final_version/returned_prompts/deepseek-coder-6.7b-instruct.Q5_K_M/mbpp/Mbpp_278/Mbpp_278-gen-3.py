
def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # Output: 3

Explanation:
The function `count_first_elements` counts the number of elements in the tuple `tup` that appear before the first tuple. It does this by iterating over the elements in `tup`, checking if each element is a tuple (using `isinstance`), and if it is, breaking out of the loop (`break`). If it's not a tuple, it increments `count`. At the end of the loop, it returns `count`.

The output of the function `count_first_elements((1, 5, 7, (4, 6), 10))` is `3` because there are three elements before the first tuple: `1`, `5`, and `7`.
"""

