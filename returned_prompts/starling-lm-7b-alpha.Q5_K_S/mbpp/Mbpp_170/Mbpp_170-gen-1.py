Here's one possible solution:

```python
def sum_range_list(nums, start_index, end_index):
  total = 0
  for i in range(start_index, end_index + 1):
    total += nums[i]
  return total
```

This solution defines a function `sum_range_list` that takes a list of numbers (`nums`), a start index (`start_index`), and an end index (`end_index`). It initializes a variable `total` to 0, and then iterates over the range of indices from `start_index` to `end_index + 1`. For each index, it adds the corresponding number to the `total`. Finally, it returns the `total`.

The assertion `assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29` is used to verify that the function correctly calculates the sum of numbers in the specified range. It should return 29 for the given input.

You can test the function with different inputs to ensure it works correctly. For example, you can try `sum_range_list([1,2,3,4,5,6,7,8,9,10], 2, 5)` to verify that it correctly calculates the sum of numbers from index 2 to index 5.

Here are some additional test cases you can try:

- `sum_range_list([1,2,3,4,5,6,7,8,9,10], 0, 2)` should return 9 (1 + 2 + 3 + 4)
- `sum_range_list([1,2,3,4,5,6,7,8,9,10], 5, 9)` should return 45 (6 + 7 + 8 + 9 + 10)
- `sum_range_list([1,2,3,4,5,6,7,8,9,10], 10, 12)` should return 0 (since there are no elements between index 1