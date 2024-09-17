```
def max_occurrences(lst):
    from collections import Counter
    counter = Counter(lst)
    return counter.most_common(1)[0][0]
```
The function `max_occurrences` uses the `Counter` class from the `collections` module to count the frequency of each item in the list. It then returns the item with the maximum frequency, which is the first item in the list of most common elements. The `most_common` method returns a list of tuples, where the first element of each tuple is the item and the second element is its frequency. The `most_common(1)` call returns a list with the most common item, and `[0][0]` extracts the item itself.

Note that the `max_occurrences` function assumes that the input list is not empty. If the input list is empty, it will raise an exception when trying to access the first element of the list. If you want to handle the case where the input list is empty, you can add a check at the beginning of the function:
```
def max_occurrences(lst):
    if not lst:
        raise ValueError("Input list is empty")
    ...
```
This will raise a `ValueError` exception with a message indicating that the input list is empty. You can modify the exception message or handle it in a different way if needed.