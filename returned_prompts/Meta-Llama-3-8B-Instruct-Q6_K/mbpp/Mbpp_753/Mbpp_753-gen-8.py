```
def min_k(records, k):
    records.sort(key=lambda x: x[1])
    return records[:k]
```
The function `min_k` takes a list of tuples `records` and an integer `k` as inputs. It sorts the records based on the second element of each tuple in ascending order. Finally, it returns the first `k` elements of the sorted list. 

For example, if you call `min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2)`, it will return `[('Akash', 2), ('Akshat', 4)]`, which are the two records with the smallest scores. 

The unit test `assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]` ensures that the function works correctly. It checks if the output of `min_k` is equal to ` [('Akash', 2), ('Akshat', 4)]` when the input is `min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2)`. If the output is not equal, the test will fail. 

This function assumes that the input list is not empty and `k` is a positive integer. If the input list is empty or `k` is not a positive integer, the function may not work correctly. You may want to add error handling to handle these cases. 