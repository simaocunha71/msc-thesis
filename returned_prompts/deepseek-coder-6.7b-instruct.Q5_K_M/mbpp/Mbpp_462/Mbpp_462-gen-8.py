
Here is the Python code for the above question.

```python
def combinations_list(lst):
    result = [[]]
    for i in lst:
        result.extend([j + [i] for j in result])
    return result

print(combinations_list(['orange',  'red',  'green',  'blue']))
```

In this function, we initialize the result as an empty list. We then go through each element in the input list. For each element, we generate a new list by extending the result list with each existing list plus the current element. Finally, we return the result.

This function works by using a technique called "list comprehension", which is a concise way to create lists in Python. The expression `j + [i]` creates a new list by appending the current element `i` to each list `j` in the result. The `extend` method then adds these new lists to the result.

The output of this function is a list of all possible combinations of the elements of the input list.

This function works by using a technique called "list comprehension", which is a concise way to create lists in Python. The expression `j + [i]` creates a new list by appending the current element `i` to each list `j` in the result. The `extend` method then adds these new lists to the result.

The output of this function is a list of all possible combinations of the elements of the input list.
"""

