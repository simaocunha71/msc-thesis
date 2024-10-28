```
def count_X(tup, element):
    return tup.count(element)
```
This function takes in a tuple and an element as arguments. It then uses the built-in `count` method of the tuple to count the occurrences of the element in the tuple. The `count` method returns the number of occurrences of the given element in the tuple. The function then returns this count.

The unit test `assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0` ensures that the function correctly returns 0 when the element does not appear in the tuple. This is because 4 does not appear in the given tuple. The function will return the correct count for the element in the tuple if it appears. For example, if the element is 8, the function will return 4 because 8 appears 4 times in the tuple. 