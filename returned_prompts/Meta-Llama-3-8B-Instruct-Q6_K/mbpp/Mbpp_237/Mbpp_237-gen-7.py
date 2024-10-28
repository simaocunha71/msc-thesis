```
def check_occurences(lst):
    from collections import Counter
    return dict(Counter(lst))
```


This problem asks you to write a function that takes a list of tuples and returns a dictionary. The dictionary should map each unique tuple to the number of times it occurs in the list.

The function should count the occurrences of each tuple in the list and then create a dictionary with the tuples as keys and their counts as values.

The unit test `assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}` helps to clarify the problem by providing an example of the expected output.

To solve this problem, you can use the `Counter` class from the `collections` module, which is a dictionary subclass for counting hashable objects. Here is the solution:
```
from collections import Counter
def check_occurences(lst):
    return dict(Counter(lst))
```
This function works by creating a `Counter` object from the input list, and then converting the `Counter` object to a dictionary using the `dict` function. The `Counter` object counts the occurrences of each tuple in the list, and the resulting dictionary maps each unique tuple to its count.