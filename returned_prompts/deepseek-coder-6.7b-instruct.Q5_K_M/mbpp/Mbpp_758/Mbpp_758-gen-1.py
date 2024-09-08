```python
def unique_sublists(lst):
    sublist_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in sublist_dict:
            sublist_dict[tuple_sublist] += 1
        else:
            sublist_dict[tuple_sublist] = 1
    return sublist_dict

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
```
The function `unique_sublists` takes a list of lists as its argument. It initializes an empty dictionary `sublist_dict`. It then iterates over each sublist in the input list. For each sublist, it converts it to a tuple `tuple_sublist` and checks if this tuple is already a key in `sublist_dict`. If it is, it increments the corresponding value by 1. If it isn't, it adds this tuple to the dictionary with a value of 1. Finally, it returns the dictionary.

The output of this function for the provided example is `{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}`, which is the expected result.

Remember to use the `tuple()` function to convert lists to tuples, and use the `in` keyword to check if a key is in a dictionary.

The `+=` operator can be used to increment the value of a key in a dictionary, and `=` can be used to set the value of a key in a dictionary.

The `for` loop can be used to iterate over each element in a list.

The `if` statement can be used to conditionally execute code.

Finally, the `return` statement is used to send back the result of a function.
