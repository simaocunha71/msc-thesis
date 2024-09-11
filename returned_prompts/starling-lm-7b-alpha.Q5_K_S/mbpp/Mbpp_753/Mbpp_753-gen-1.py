```
def min_k(tup_list, k):
    tup_list.sort(key = lambda x : x[1])
    return tup_list[:k]

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
```

Explanation:
The function `min_k` first sorts the tuple list based on the second element in each tuple, in ascending order. It uses a lambda function as the key to sort the list. Then, it returns the first k tuples from the sorted list.

In the given test case, the tuple list `[('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]` is sorted based on the second element in each tuple. The sorted list is `[('Akash', 2), ('Akshat', 4), ('Manjeet', 10), ('Nikhil', 8)]`. The function returns the first 2 tuples, which are `[('Akash', 2), ('Akshat', 4)]`. The assert statement checks if the function returns the expected result.

In Python, the `sort` method sorts the list in-place, modifying the original list. The `key` parameter of the `sort` method takes a function that is used to specify a different comparison criterion. In this case, the lambda function `lambda x : x[1]` is used to sort the list based on the second element in each tuple.

The `[:k]` notation is used to slice the list and return the first k elements.

Overall, the function `min_k` finds the minimum k records from a tuple list based on the second element in each tuple, and returns them as a new list.

Here are some additional notes:
- The lambda function `lambda x : x[1]` is an anonymous function that takes a single argument `x` and returns the second element of `x` (`x[1]`). It is used as the key function