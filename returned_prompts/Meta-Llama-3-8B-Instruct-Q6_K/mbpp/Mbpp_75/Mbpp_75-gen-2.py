```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```


This function uses a list comprehension to iterate over the input list of tuples. For each tuple, it checks if all elements are divisible by k using the `all` function and a generator expression. If all elements are divisible by k, the tuple is included in the output list. The function returns a list of tuples that have all elements divisible by k. 





The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function works correctly. It checks that the output of the function is `[(6, 24, 12)]` when the input is `[(6, 24, 12), (7, 9, 6), (12, 18, 21)]` and `k` is `6`. This test passes if the function is implemented correctly.