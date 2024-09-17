```
def merge(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    return [first_elements, second_elements]
```


The given problem is asking to create a function that takes a list of lists as an input, where each sublist contains two elements. The function should return a list of two lists. The first list should contain the first element of each sublist, and the second list should contain the second element of each sublist.

To solve this problem, we can use list comprehension. List comprehension is a concise way to create lists in Python. It is a shorthand for a for loop that iterates over a list and constructs a new list from the results of the loop.

Here is the solution:

```
def merge(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    return [first_elements, second_elements]
```

This function works by iterating over each sublist in the input list of lists. For each sublist, it takes the first element and adds it to the `first_elements` list, and it takes the second element and adds it to the `second_elements` list. Finally, it returns a list containing these two lists.

The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` helps to clarify the expected output of the function. It shows that the function should take each sublist and add its elements to the corresponding list in the output. For example, the sublist `['x', 'y']` should add `x` to the first list and `y` to the second list. The sublist `['a', 'b']` should add `a` to the first list and `b` to the second list, and so on. The function should return a list containing these two lists.