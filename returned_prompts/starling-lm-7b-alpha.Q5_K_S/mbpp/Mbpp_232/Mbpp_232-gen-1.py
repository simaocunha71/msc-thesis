Here's one possible solution:

```python
def larg_nnum(num_list, n):
    # Sort list in descending order
    sorted_list = sorted(num_list, reverse=True)
    # Return the first n largest numbers
    return sorted_list[:n]
```

This solution first sorts the input list in descending order using the `sorted()` function with the `reverse=True` parameter. Then, it returns a slice of the sorted list containing the first `n` elements. 

The assertion `set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` checks if the function correctly returns the two largest numbers from the given list. The output should be `True` if the function is working correctly.

You can use this function to find the `n` largest items in any given list.

```python
largest_nums = larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)
print(largest_nums)  # Output: [100, 90]
```

This will print the two largest numbers from the list `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]`, which are `[100, 90]`.

```python
def larg_nnum(num_list, n):
    # Sort list in descending order
    sorted_list = sorted(num_list, reverse=True)
    # Return the first n largest numbers
    return sorted_list[:n]
```

This solution first sorts the input list in descending order using the `sorted()` function with the `reverse=True` parameter. Then, it returns a slice of the sorted list containing the first `n` elements.