```
def check_occurences(lst):
    from collections import Counter
    return dict(Counter(lst))
```


The problem is asking to create a function that takes a list of tuples and returns a dictionary where each unique tuple is mapped to the number of times it appears in the list.

The unit test `assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}` suggests that the order of the tuples in the dictionary does not matter.

To solve this problem, we can use the `Counter` class from the `collections` module, which is a dictionary subclass for counting hashable objects. We can convert the list of tuples to a `Counter` object and then convert it back to a dictionary.

Here's the solution:
```
def check_occurences(lst):
    from collections import Counter
    return dict(Counter(lst))
```
This function takes a list of tuples as input, converts it to a `Counter` object, and then converts it back to a dictionary. The resulting dictionary maps each unique tuple to the number of times it occurs in the list. The order of the tuples in the dictionary is not guaranteed, but the count of each tuple is accurate.