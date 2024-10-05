```
def largest_smallest_integers(lst):
    negative_integers = [x for x in lst if x < 0]
    positive_integers = [x for x in lst if x > 0]
    
    if negative_integers:
        largest_negative = max(negative_integers)
    else:
        largest_negative = None
    
    if positive_integers:
        smallest_positive = min(positive_integers)
    else:
        smallest_positive = None
    
    return largest_negative, smallest_positive
```



The function `largest_smallest_integers` takes a list of integers as input. It first filters the list to get all negative integers and all positive integers. Then, it checks if either list is not empty. If a list is not empty, it finds the maximum value in the list of negative integers and the minimum value in the list of positive integers. If a list is empty, it sets the corresponding value in the return tuple to `None`. Finally, it returns the tuple `(largest_negative, smallest_positive)`. 