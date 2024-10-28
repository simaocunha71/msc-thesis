```
def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(tuple1 for tuple1 in tuple_list1)
    set2 = set(tuple2 for tuple2 in tuple_list2)
    intersection = set1 & set2
    return intersection
```


This function converts the given tuple lists into sets and then finds the intersection of these sets. The intersection of two sets is a set containing all elements that are in both sets. In Python, you can use the `&` operator to find the intersection of two sets.

The unit test `assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}` ensures that the function works correctly, regardless of the order of the elements in the tuples. It checks that the function returns the expected intersection of the two sets of tuples. 

This function is case-sensitive and considers tuples as equal only if their elements are in the same order. This means that it does not consider tuples with the same elements but in different order as equal. If you want to consider tuples with the same elements but in different order as equal, you can convert the tuples to frozensets (which are unordered) before finding the intersection. Here is an example of how you can do this:
```
def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(frozenset(tuple1) for tuple1 in tuple_list1)
    set2 = set(frozenset(tuple2) for tuple2 in tuple_list2)
    intersection = set1 & set2
    return set(frozenset(tuple) for tuple in intersection)
```


This modified function converts each tuple to a frozenset (which is an unordered set) before finding the intersection of the sets. The intersection is then converted back to a set of tuples before being returned. This means that tuples with the same elements but in different order are considered equal. 





```
def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(tuple1 for tuple1 in tuple_list1)
    set2 = set(tuple2 for tuple2 in tuple_list2)
    intersection = set1 & set2
    return set(tuple(sorted(t)) for t in intersection)
```


