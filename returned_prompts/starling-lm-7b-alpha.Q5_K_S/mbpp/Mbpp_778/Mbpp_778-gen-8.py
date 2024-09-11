Here's a solution in Python:

```python
def pack_consecutive_duplicates(nums):
    res = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            res.append([nums[i]])
        else:
            res[-1].append(nums[i])
    return res
```

This function `pack_consecutive_duplicates` takes in a list of numbers (`nums`) and returns a new list of sublists where consecutive duplicates of the numbers in the original list are packed into sublists. 

The function iterates over the input list using a `for` loop and checks if the current element (`nums[i]`) is the same as the previous element (`nums[i - 1]`). If they are different, a new sublist is created and the current element is added to it. If they are the same, the current element is appended to the last sublist. 

Finally, the function returns the resulting list of sublists. 

The assertion `assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]` checks if the function correctly packs the consecutive duplicates of the given list.

You can test the function with different inputs to ensure it works as expected.

```python
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))  # Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7],