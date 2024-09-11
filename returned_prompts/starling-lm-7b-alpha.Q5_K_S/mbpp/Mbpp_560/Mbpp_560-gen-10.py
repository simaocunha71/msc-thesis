```
def union_elements(tup1, tup2):
    res = list(tup1)
    for i in tup2:
        if i not in res:
            res.append(i)
    res.sort()
    return tuple(res)
```

Explanation:

The function `union_elements` takes two tuples as input and creates a list `res` from the first tuple. Then it iterates over each element of the second tuple and checks if it is not already in the list. If not, it appends the element to the list. Finally, the list is converted back to a tuple and sorted, and the sorted tuple is returned as the result.

The provided assertion `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` checks if the function correctly finds the union of the elements in the two tuples and sorts them. The expected output is `(3, 4, 5, 6, 7, 10)`.

The output of the function is a tuple containing the elements of both tuples in sorted order.

Note: The `if i not in res` check ensures that duplicate elements are not added to the result.

Here's an example usage of the function:
```
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10) ))
# Output: (3, 4, 5, 6, 7, 10)
```

This will output the union of the elements in the two tuples, sorted in ascending order: `(3, 4, 5, 6, 7, 10)`.

You can use this function to find the union of any two tuples and output the result in sorted order.

"""
```

python

```python
def union_elements(tup1, tup2):
    res = list(tup1)
    for i in tup2:
        if i not in res:
            res.append(i)
    res.