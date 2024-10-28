```
def find_tuples(tuples_list, k):
    return [tuple for tuple in tuples_list if all(i % k == 0 for i in tuple)]
```


The function `find_tuples` takes a list of tuples and an integer `k` as input, and returns a list of tuples where all elements are divisible by `k`. It uses a list comprehension to iterate over each tuple in the input list, and checks if all elements in the tuple are divisible by `k` using the `all` function and a generator expression. If all elements are divisible by `k`, the tuple is included in the output list. 

The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function works correctly. It checks that the output of the function when given the input `[(6, 24, 12), (7, 9, 6), (12, 18, 21)]` and `6` is `[(6, 24, 12)]`, which is the expected output because the only tuple in the input list that has all elements divisible by `6` is `(6, 24, 12)`. 