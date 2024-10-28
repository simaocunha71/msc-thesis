You can use the following function:

```python
def monotonic(l: list):
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return increasing or decreasing
```

This function works by first checking if the list is monotonically increasing (`increasing`) and then checking if it is monotonically decreasing (`decreasing`). If either condition is true, the function returns `True`. If neither condition is true, the function returns `False`.

Here's an explanation of how the function works:

1. `all(l[i] <= l[i+1] for i in range(len(l)-1))`: This line checks if the list is monotonically increasing. It does this by checking each pair of adjacent elements in the list. If the current element is less than or equal to the next element, the function continues to the next pair of elements. If any pair of elements is such that the current element is greater than the next element, the function returns `False`. If all pairs of elements satisfy this condition, the function returns `True`.

2. `all(l[i] >= l[i+1] for i in range(len(l)-1))`: This line checks if the list is monotonically decreasing. It does this by checking each pair of adjacent elements in the list. If the current element is greater than or equal to the next element, the function continues to the next pair of elements. If any pair of elements is such that the current element is less than the next element, the function returns `False`. If all pairs of elements satisfy this condition, the function returns `True`.

3. `return increasing or decreasing`: This line returns `True` if either the list is monotonically increasing or decreasing, and `False` otherwise.

The function uses the `all` function to check if all elements in the list satisfy a certain condition. The `all` function takes an iterable as an argument and returns `True` if all elements in the iterable are true, and `False` otherwise.

The function also uses a generator expression to iterate over the list and check each pair of adjacent elements. The generator expression is `l[i] <= l[i+1] for i in range(len(l)-1)`, which generates a sequence of boolean values indicating whether each pair of adjacent elements satisfies the condition. The `all` function then checks