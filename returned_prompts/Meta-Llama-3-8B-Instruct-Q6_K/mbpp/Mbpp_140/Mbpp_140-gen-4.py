```
def extract_singly(lst_of_lists):
    return set(sum((x for sublist in lst_of_lists for x in sublist), []))
```
The function `extract_singly` takes a list of lists as input and returns a set of unique numbers. It uses a generator expression to flatten the list of lists into a single iterable of numbers, and then converts that iterable into a set to remove any duplicates.

The unit test `assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])` ensures that the function works correctly. It checks that the output of `extract_singly` is a set containing the numbers 1, 3, 4, 5, and 7, which are the unique elements in the input list of lists.