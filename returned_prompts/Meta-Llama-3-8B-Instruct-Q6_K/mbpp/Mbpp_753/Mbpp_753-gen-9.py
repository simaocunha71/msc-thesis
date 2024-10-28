```
def min_k(tuples, k):
    return sorted(tuples, key=lambda x: x[1])[:k]
```
This function sorts the input list of tuples based on the second element of each tuple (i.e., the value), and then returns the first k elements of the sorted list. This effectively returns the k smallest values from the input list.

For example, if the input list is `[('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]` and k is `2`, the function will return `[('Akash', 2), ('Akshat', 4)]`, which are the two smallest values in the input list. 

The unit test `assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]` confirms that the function returns the correct result for this input. 