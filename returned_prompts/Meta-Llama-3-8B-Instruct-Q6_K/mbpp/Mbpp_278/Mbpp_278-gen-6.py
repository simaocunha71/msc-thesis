You want a function that counts the number of elements in a tuple that occur before a specific element in the tuple. The specific element is a tuple itself, not just a single value.

Looking at the unit test `assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3`, we can see that the function should return `3` because `1`, `5`, and `7` occur before `(4, 6)` in the tuple.

Here's a Python function that solves this problem:
```
def count_first_elements(t):
    count = 0
    for x in t:
        if not isinstance(x, tuple):
            count += 1
        else:
            return count
    return count
```
This function iterates over the elements in the tuple. If an element is not a tuple, it increments the count. If it finds a tuple, it returns the count. If the tuple is at the end of the list, it returns the total count of non-tuple elements.