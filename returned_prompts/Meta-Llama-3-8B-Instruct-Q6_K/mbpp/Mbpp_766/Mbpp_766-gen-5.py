```
def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst) - 1)]
```


The function `pair_wise` takes a list as input and returns a list of tuples. Each tuple contains two consecutive elements from the input list. The function uses a list comprehension to generate the list of pairs. The range of the list comprehension is from 0 to the second last index of the input list (since we need to consider consecutive elements). The `lst[i]` and `lst[i+1]` are used to get the consecutive elements and they are combined into a tuple.

The unit test `assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]` ensures that the function works correctly. It checks if the output of the function `pair_wise([1,1,2,3,3,4,4,5])` is as expected. If the function works correctly, the assertion will pass, otherwise, it will raise an AssertionError.