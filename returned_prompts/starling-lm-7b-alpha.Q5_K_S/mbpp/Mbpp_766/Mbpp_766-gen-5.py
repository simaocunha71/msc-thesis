def pair_wise(nums):
    return list(zip(nums[:-1], nums[1:]))


# Alternative Solution
def pair_wise_alternative(nums):
    return [(nums[i], nums[i+1]) for i in range(len(nums)-1)]


```

Explanation:

The first solution uses the built-in zip function in Python to combine each item in the list with its consecutive item. The zip function takes in two or more iterables and returns an iterator that generates tuples containing elements from each iterable. By slicing the input list nums[:-1] and nums[1:], we can create two iterables that contain all but the last item and all but the first item of the original list, respectively. These two iterables are then zipped together to create a list of pairs of consecutive items.

The second solution is an alternative approach that uses list comprehension. It iterates over the range of the length of the input list minus one, which gives us the indices of all but the last item in the list. For each index i, it creates a tuple with the item at index i and the item at index i+1, and appends it to a new list.

Both solutions return a list of pairs of consecutive items in the given list, and they produce the same result as the provided assertion for the sample input [1,1,2,3,3,4,4,5].

```python
def pair_wise(nums):
    return list(zip(nums[:-1], nums[1:]))

# Testing the function
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
print("All tests passed")
```

In the above code, the function `pair_wise` is defined and tested. The `assert` statement checks if the function returns the expected result for the provided sample input. If the assertion passes, the message "All tests passed" is printed.

You can add more test cases by modifying the