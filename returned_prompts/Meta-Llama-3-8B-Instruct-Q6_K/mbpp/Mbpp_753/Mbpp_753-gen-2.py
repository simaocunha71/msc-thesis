```
def min_k(tuples, k):
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    return sorted_tuples[:k]
```


The function works by first sorting the list of tuples based on the second element of each tuple (i.e., the values). It then returns the first k elements of the sorted list, which are the k smallest values. This is because the list is sorted in ascending order by default, so the first elements will be the smallest.

For example, if you call `min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2)`, the function will return ` [('Akash', 2), ('Akshat', 4)]`, which are the two smallest values in the list.