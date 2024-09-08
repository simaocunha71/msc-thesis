```python
def round_and_sum(nums):
    return sum(round(n) for n in nums) * len(nums)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
```

Output:
```
243
```

Explanation:

In the function, we use a generator comprehension to iterate over each number in the input list and round it. We then sum up these rounded numbers and multiply the result by the length of the list. The built-in function round() is used to round the numbers. The function sum() is used to compute the sum of the numbers, and the len() function is used to find the length of the list.

This solution should work for any list of numbers, as it doesn't have any hard-coded values. The result will be the same regardless of the numbers in the input list.
"""

def round_and_sum(nums):
    return sum(round(n) for n in nums) * len(nums)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
```

Output:
```
243
```

Explanation:

In the function, we use a generator comprehension to iterate over each number in the input list and round it. We then sum up these rounded numbers and multiply the result by the length of the list. The built-in function round() is used to round the numbers. The function sum() is used to compute the sum of the numbers, and the len() function is used to find the length of the list.

This solution should work for any list of numbers, as it doesn't have any hard-coded values. The result will be the same regardless of the numbers in the input list.
"""

def round_and_sum(nums