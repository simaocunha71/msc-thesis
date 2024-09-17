```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```



The given problem is to write a function that takes a list of tuples and an integer k as input, and returns a list of tuples where all elements in each tuple are divisible by k.

The unit test provided is:
```
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
```

This test suggests that the function should return a list of tuples where all elements in each tuple are divisible by 6. The expected output is `[(6, 24, 12)]`.

Here is the solution:
```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```

This function uses a list comprehension to iterate over the input list of tuples. For each tuple, it uses the `all` function with a generator expression to check if all elements in the tuple are divisible by k. If they are, the tuple is included in the output list. If not, it is skipped. The function returns the list of tuples that meet the condition.