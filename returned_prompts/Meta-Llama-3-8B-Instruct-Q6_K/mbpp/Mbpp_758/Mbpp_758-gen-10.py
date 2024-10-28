```
def unique_sublists(lst):
    tuples = set()
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in tuples:
            tuples.add(tuple_sublist)
    return {k: lst.count(k) for k in tuples}
```



The function `unique_sublists` takes a list of lists as input and returns a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurrences in the original list.

The function works by iterating over each sublist in the input list and converting it to a tuple. If the tuple is not already in the set `tuples`, it is added. This ensures that each unique sublist is only counted once.

Finally, the function iterates over the set `tuples` and counts the number of occurrences of each tuple in the original list using the `count` method. The result is a dictionary where each key is a unique tuple and the value is the number of times it occurs in the original list.

The unit test `assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}` ensures that the function works correctly. It checks that the function returns the correct dictionary for a given input list. If the function is implemented correctly, this unit test should pass.