```
def largest_subset(nums):
    '''
    Given a list of numbers, find the size of the largest subset so that every pair is divisible.
    '''
    max_size = 0
    for num in nums:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            max_size += 1
        else:
            if max_size > 0:
                max_size = 0
    return max_size
```

Here are the steps in the function:

1. Initialize a variable `max_size` to 0, which will store the size of the largest subset of divisible pairs.
2. Iterate through the list of numbers `nums`.
3. Check if the current number is divisible by 2 (i.e., even). If it is, increment `max_size` by 1. If it's not, set `max_size` to 0.
4. Repeat steps 2-3 for all numbers in `nums`.
5. Return the final value of `max_size`, which represents the size of the largest subset of divisible pairs.

This function counts the number of even numbers in the input list, as these are the only numbers that can be part of a divisible pair. Since every odd number would break the divisibility requirement, the function sets `max_size` to 0 whenever it encounters an odd number. As a result, the final value of `max_size` represents the size of the largest subset of divisible pairs in the input list.

The time complexity of this function is O(n), where n is the length of the input list, as it iterates through the list only once. The space complexity is O(1), as it uses a single variable `max_size` to store the result.

Here are some test cases for the function:

```python
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
assert largest_subset([2, 4, 6, 8]) == 4
assert largest_subset([1, 3, 5, 7, 9]) == 0
```

These test cases