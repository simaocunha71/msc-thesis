```
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


This function uses list comprehensions to separate the input list into two lists: one for negative integers and one for positive integers. It then checks if each list is not empty. If it's not empty, it finds the largest negative integer and the smallest positive integer using the max and min functions respectively. If either list is empty, it sets the corresponding variable to None. Finally, it returns the two variables as a tuple. 

For example, `largest_smallest_integers([2, 4, 1, 3, 5, 7])` will return `(None, 1)` because there are no negative integers in the list. `largest_smallest_integers([])` will return `(None, None)` because there are no negative or positive integers in the list. `largest_smallest_integers([0])` will return `(None, None)` because there are no negative or positive integers in the list, only zeros. 