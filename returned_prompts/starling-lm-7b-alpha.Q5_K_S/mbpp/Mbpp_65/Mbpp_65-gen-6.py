from functools import reduce
def recursive_list_sum(lst):
    # using reduce to sum all elements in the flattened list
    return reduce(lambda x, y: x + y, [i for sublist in lst for i in sublist])


# Test Case
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
print("All Test Cases Passed")




"""
The function recursive_list_sum(lst) takes a nested list of numbers as its input and uses the reduce function from the functools module to add all the numbers in the flattened list together.

The function uses a list comprehension to flatten the nested list, and then uses the reduce function to add all the elements in the flattened list together. The lambda function in the reduce function adds the current element with the accumulated sum.

The recursive_list_sum function is tested with the example input [1, 2, [3,4],[5,6]] and the expected output is 21. The assert statement checks if the output of recursive_list_sum(lst) is equal to 21. If the assertion is true, the message "All Test Cases Passed" is printed.
"""











































```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``