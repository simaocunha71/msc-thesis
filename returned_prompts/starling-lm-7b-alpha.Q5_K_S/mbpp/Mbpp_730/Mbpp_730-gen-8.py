def consecutive_duplicates(list):
    prev = None
    res = []
    for x in list:
        if prev is None or x != prev:
            res.append(x)
        prev = x
    return res

# Test
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

# Expected Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""
The time complexity of this function is O(n) where n is the number of elements in the given list.
For each element, we compare it to the previous element and add it to the result if it's not a duplicate.
This means we only traverse the list once.
"""

"""
The space complexity of this function is O(n) where n is the number of elements in the given list.
We need to store all the non-duplicate elements in a result list, which may have the same size as the input list.
"""

"""
The space complexity can be improved to O(1) if we don't need the result list.
We can simply output the result as we traverse the list without storing it in a separate list.
"""

"""
Also, we can optimize the code to remove the previous element check.
Instead of checking if x != prev, we can directly append x to the result list if prev is None.
This way, we don't need to keep track of the previous element, reducing the space complexity to O(1).
"""

"""
We can further optimize the code to remove the need for the previous element check.
Instead of checking if x != prev, we can directly append x to the result list if prev is None.
This way, we don't need to keep track of the previous element, reducing the space complexity to O(1).
"""

```python
def consecutive_duplicates(list):
    prev = None
    res = []
    for x in list:
        if prev is