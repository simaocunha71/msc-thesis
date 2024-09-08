"""
We will use zip function to iterate over three lists simultaneously. We will check if all three lists have the same value at the same index. If they do, we will append the value to the result list.
"""

def extract_index_list(l1, l2, l3):
    result = []
    for i1, i2, i3 in zip(l1, l2, l3):
        if i1 == i2 == i3:
            result.append(i1)
    return result

print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

# Output: [1, 7]
```

# Explanation:
The function `extract_index_list` takes three lists `l1`, `l2`, `l3` as arguments. It initializes an empty list `result`.

Then it iterates over `l1`, `l2`, and `l3` simultaneously using the `zip` function. For each iteration, it checks if the current elements in `l1`, `l2`, and `l3` are equal. If they are, it appends the common element to `result`.

Finally, it returns the `result` list which contains all common elements from `l1`, `l2`, and `l3`.

# Test Case:
The provided test case `[1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]` should return `[1, 7]` as the common elements at the same index in all three lists are `1` and `7`.

# Edge Cases:
If the lists have different lengths, the function will only consider the common elements up to the length of the shortest list.

If there are no common elements, the function will return