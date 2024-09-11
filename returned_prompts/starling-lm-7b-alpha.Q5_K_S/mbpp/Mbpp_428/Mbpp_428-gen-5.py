Here's one way you can implement Shell Sort in Python:

```python
def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums
```

This function takes an input list `nums` and sorts it using Shell Sort. The `gap` variable is initially set to half the length of the input list. The algorithm then repeatedly compares and swaps elements in the list until the list is fully sorted. The `gap` is then halved until it is less than 1, at which point the sorting is complete.

You can test the function with the provided assertion like this:

```python
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```

This assertion checks if the `shell_sort` function correctly sorts the given list. If the assertion passes, it means that the function is working correctly.

Here's a step-by-step breakdown of how the `shell_sort` function works:

1. Initialize the `gap` variable to half the length of the input list.
2. Enter a while loop that continues until the `gap` becomes 0.
3. Within the while loop, enter a for loop that iterates over the elements starting from the `gap` index until the end of the list.
4. For each element, store its value in a temporary variable `temp` and set the index `j` to the current element's index.
5. Enter a while loop that continues until `j` is less than the `gap` and the element at index `