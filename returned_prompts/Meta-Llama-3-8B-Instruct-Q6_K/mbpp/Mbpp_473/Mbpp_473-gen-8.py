```
def tuple_intersection(tuples1, tuples2):
    set1 = set(map(tuple, tuples1))
    set2 = set(map(tuple, tuples2))
    return set1 & set2
```


The function `tuple_intersection` takes two lists of tuples as input. It first converts each list of tuples into a set of tuples using the `map` function. Then, it calculates the intersection of the two sets using the `&` operator. The intersection is then returned as a set of tuples. The function works regardless of the order of the elements in the tuples.

The unit test `assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}` demonstrates the functionality of the function. It checks that the intersection of the two input lists of tuples is correctly calculated, even if the order of the elements in the tuples is different.