The task is to create a function that finds the largest negative integer and the smallest positive integer in a given list. If the list does not contain any negative or positive integers, the function should return None for both values.

Here is a Python function that solves this problem:

```Python
def largest_smallest_integers(lst):
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if negatives:
        largest_negative = max(negatives)
    else:
        largest_negative = None

    if positives:
        smallest_positive = min(positives)
    else:
        smallest_positive = None

    return largest_negative, smallest_positive
```

This function uses list comprehensions to create lists of negative and positive integers from the input list. It then checks if these lists are not empty, and if they are not, it finds the maximum value in the list of negatives (or None if it is empty) and the minimum value in the list of positives (or None if it is empty). Finally, it returns a tuple containing these two values.

For example, if you call `largest_smallest_integers([2, 4, 1, 3, 5, 7])`, the function will return `(None, 1)`, because there are no negative integers in the list, and the smallest positive integer is 1. If you call `largest_smallest_integers([0])`, the function will return `(None, None)`, because there are no negative or positive integers in the list. If you call `largest_smallest_integers([])`, the function will also return `(None, None)`, because there are no integers in the list.