def pair_wise(nums):
    out = []
    for i in range(len(nums)-1):
        out.append((nums[i],nums[i+1]))
    return out


# Alternative:
# def pair_wise(nums):
#     return [(nums[i],nums[i+1]) for i in range(len(nums)-1)]


```
The above code defines a function `pair_wise` which takes a list of numbers as its input and returns a list of all pairs of consecutive items in the input list. The function uses a for loop to iterate over the input list and appends each pair of consecutive items to the `out` list. Finally, the function returns the `out` list.

The alternative version of the function uses list comprehension to achieve the same result. It creates a new list by iterating over the input list and appending each pair of consecutive items. This version is more concise and readable, but may be slightly slower than the for loop version.
```

```python
# Testing the function:
print(pair_wise([1,1,2,3,3,4,4,5]))  # Expected output: [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
```

The `assert` statement is used to verify the correctness of the function. It compares the output of the `pair_wise` function with the expected output and asserts that they are equal. If the assertion fails, an error will be raised.
```

```python
# Wrong implementation of the function:
def pair_wise_wrong(nums):
    out = []
    for i in range(len(nums)):
        out.append((nums[i],nums[i+1]))
    return out
```

The wrong implementation of the function `pair_wise_wrong` has a minor mistake. It uses the `range(len(nums))` instead of `range(len(nums)-1)` in the for loop, which results in an index out of range error