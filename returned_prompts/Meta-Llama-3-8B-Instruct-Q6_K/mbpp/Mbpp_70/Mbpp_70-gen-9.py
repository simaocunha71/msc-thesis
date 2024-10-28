```
def get_equal(tuples):
    return len(set(len(i) for i in tuples)) == 1
```


This function uses the set data structure to find the unique lengths of the tuples. If the set contains only one element, it means all tuples have the same length. If the set contains more than one element, it means the tuples have different lengths. The function returns True if all tuples have equal length, and False otherwise.

The unit test `assert get_equal([(11, 22, 33), (44, 55, 66)]) == True` ensures that the function returns True when all tuples have equal length. 