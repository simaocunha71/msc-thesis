```
def find_tuples(tuples, k):
    result = [t for t in tuples if all(i % k == 0 for i in t)]
    return result
```


The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function correctly identifies tuples with all elements divisible by k. The function uses a list comprehension to iterate over the input tuples and check if all elements in each tuple are divisible by k. The `all` function returns `True` if all elements in the iterable are true. If all elements in a tuple are divisible by k, the tuple is added to the result list. The function returns the list of tuples that have all elements divisible by k.