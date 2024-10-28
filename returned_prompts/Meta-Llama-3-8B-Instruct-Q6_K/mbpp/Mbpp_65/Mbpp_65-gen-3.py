The problem is asking to create a function that takes a list as input, flattens it (i.e., converts any nested lists into a single list), and then sums up all the elements in the flattened list.

The unit test `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21` suggests that the function should be able to handle nested lists, and that the sum should be returned as the result.

Here is a Python solution using a recursive approach:

```
def recursive_list_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += recursive_list_sum(elem)
        else:
            total += elem
    return total
```

This function works by iterating over each element in the input list. If the element is a list itself, the function calls itself with that element as the new input, effectively flattening the list. If the element is not a list, it is added to the total sum. The function returns the total sum at the end.