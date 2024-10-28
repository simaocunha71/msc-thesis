```
def average_tuple(tuples):
    result = []
    for tup in tuples:
        result.append(sum(tup) / len(tup))
    return result
```


The function takes a tuple of tuples as input. For each tuple, it calculates the average by summing all the elements and dividing by the number of elements. The results are stored in a list and returned. The unit test provided ensures that the function works correctly.