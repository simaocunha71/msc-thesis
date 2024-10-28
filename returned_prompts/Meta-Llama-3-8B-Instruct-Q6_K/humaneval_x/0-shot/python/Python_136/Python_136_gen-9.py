```
def largest_smallest_integers(lst):
    negative = [x for x in lst if x < 0]
    positive = [x for x in lst if x > 0]
    if negative:
        largest_negative = max(negative)
    else:
        largest_negative = None
    if positive:
        smallest_positive = min(positive)
    else:
        smallest_positive = None
    return largest_negative, smallest_positive
```
This function first filters the list to get the negative and positive integers. Then it checks if the lists are not empty, and if they are not, it finds the largest negative and smallest positive integers using the max and min functions. If the lists are empty, it sets the largest negative and smallest positive integers to None. Finally, it returns a tuple containing the largest negative and smallest positive integers. If both lists are empty (i.e., the input list contains only zeros or no integers), it returns (None, None). Otherwise, it returns the largest negative integer and the smallest positive integer.