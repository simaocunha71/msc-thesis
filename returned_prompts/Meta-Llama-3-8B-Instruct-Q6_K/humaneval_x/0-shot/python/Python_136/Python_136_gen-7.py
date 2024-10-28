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


This function uses list comprehension to filter out the negative and positive integers from the input list. It then checks if the resulting lists are not empty. If they are not empty, it finds the maximum value in the negative list and the minimum value in the positive list. If the lists are empty, it sets the corresponding values in the tuple to None. The function returns the tuple containing the largest negative integer and the smallest positive integer. If there are no negative or positive integers, it returns (None, None).