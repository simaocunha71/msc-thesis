```
def larg_nnum(lst,n):
    lst = sorted(lst,reverse=True)
    return lst[:n]

assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
```

The function `larg_nnum` takes in a list and an integer `n` and returns a list containing the `n` largest items from the list. It first sorts the list in descending order using the `sorted` function with the `reverse=True` argument. Then, it slices the sorted list to only include the first `n` elements. Finally, it returns the resulting list. The `assert` statement verifies that the function correctly returns the set of the two largest numbers from the given list.

Here's an example usage of the `larg_nnum` function:

```python
numbers = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
n = 2
result = larg_nnum(numbers, n)
print(result)  # Output: [100, 90]
```

In this example, the `numbers` list contains 11 integers, and we want to find the two largest numbers in the list. We call the `larg_nnum` function with the `numbers` list and `n=2` as arguments. The function correctly returns a list `[100, 90]` which are the two largest numbers in the `numbers` list.

The time complexity of this function is O(n log n) due to the sorting step, and the space complexity is O(n) to store the sorted list.

Note: It's important to sort the list in descending order to find the largest numbers. If we were to sort the list in ascending order, the resulting list would contain the `n` smallest numbers instead of the `n` largest numbers.

Additionally, it's