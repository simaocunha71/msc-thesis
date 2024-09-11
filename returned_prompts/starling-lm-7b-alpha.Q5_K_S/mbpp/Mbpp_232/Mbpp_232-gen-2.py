```
def larg_nnum(nums, n):
    nums.sort(reverse=True)
    return nums[:n]
```

Explanation:

Here's a function that takes in a list and an integer n and returns a list containing the n largest items from the list.

In the function `larg_nnum`, we first sort the input list `nums` in reverse order using the `sort()` method with `reverse=True`. This ensures that the largest numbers appear at the beginning of the list.

Then, we use slicing to return a new list that contains only the first `n` elements of the sorted `nums` list. This new list will contain the `n` largest items from the original list.

The provided assertion verifies the correctness of the function by comparing the set of the result of `larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)` with the set `[100, 90]`. Since the function correctly selects the two largest numbers from the list, the assertion passes.

To use the function, you can simply call it with the desired list and the value of `n`. For example, `larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)` will return `[100, 90]` as expected.

It's worth noting that this solution modifies the original list by sorting it in place. If you want to keep the original list unchanged, you can make a copy of the list using the `copy()` method before sorting. For example, you can modify the function as follows:

```python
def larg_nnum(nums, n):
    sorted_nums = nums.copy()
    sorted_nums.sort(reverse=True)
    return sorted_nums[:n]
```

This way, the original list `nums` will remain unchanged, and a new