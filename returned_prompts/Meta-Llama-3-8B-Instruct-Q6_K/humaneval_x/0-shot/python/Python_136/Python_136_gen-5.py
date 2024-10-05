
```
def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    return (max(negatives) if negatives else None, min(positives) if positives else None)
```

Explanation:
We use list comprehensions to create lists of negative and positive integers from the input list. Then, we use the built-in `max` and `min` functions to find the largest negative and smallest positive integers, respectively. If the lists are empty (i.e., there are no negative or positive integers), we return `None` for that value. Finally, we return a tuple containing the largest negative and smallest positive integers. If one or both of these values are `None`, that means there were no negative or positive integers in the input list.