Here is one possible solution. It sorts the list in descending order and returns the first n elements.

```python
def larg_nnum(num_list,n):
    num_list.sort(reverse=True)
    return num_list[:n]
```

Here's a breakdown of what the function does:

- The function `larg_nnum` takes in two parameters: `num_list`, which is the list of numbers, and `n`, which is the number of largest items we want in our output list.

- The function first sorts the `num_list` in descending order using the `sort()` method with the `reverse=True` parameter. This ensures that the largest numbers appear first in the list.

- Finally, the function uses list slicing (`num_list[:n]`) to return a new list containing the first `n` elements of the sorted `num_list`. These elements are the `n` largest numbers in the original list.

To test the function, we use the `set()` function to compare the result with the expected output. In this case, the expected output is the set `{100, 90}`. We can verify that the function is working correctly by checking if the set of the returned list is equal to the expected set using the `==` operator.

The output of this function is a list containing the `n` largest items from the input list, sorted in descending order.

```python
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))
```

This will output: `[100, 90]`

This confirms that the function is correctly returning the `n` largest items from the input list.

```python
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
```

This assertion passes, indicating that the function `