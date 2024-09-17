```
def combinations_list(lst):
    import itertools
    result = []
    for r in range(len(lst) + 1):
        result.extend(itertools.combinations(lst, r))
    return [list(x) for x in result]
```


The function `combinations_list` uses the `itertools.combinations` function to generate all possible combinations of the elements of the given list. The function iterates over all possible lengths of combinations, from 0 to the length of the list, and for each length, it generates all combinations of that length using `itertools.combinations`. The result is then converted to a list of lists.

The unit test `assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]` ensures that the function generates all possible combinations of the elements of the given list.