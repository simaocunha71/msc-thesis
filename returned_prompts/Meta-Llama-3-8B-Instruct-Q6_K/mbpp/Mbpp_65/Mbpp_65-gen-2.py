The problem is asking you to create a function that takes a list as input, flattens it (i.e., converts any sublists into single elements), and then returns the sum of all the elements in the flattened list.

Here's a Python solution using recursion:

```Python
def recursive_list_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total
```

This function works by iterating over each element in the input list. If the element is a list itself, it recursively calls itself on that sublist and adds the result to the total. If the element is not a list, it simply adds it to the total. The function returns the total sum of all elements in the flattened list. 

For example, if you call `recursive_list_sum([1, 2, [3,4],[5,6]])`, it will return `21`, which is the sum of all the elements in the flattened list `[1, 2, 3, 4, 5, 6]`. This is verified by the provided unit test.  `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21` passes. 