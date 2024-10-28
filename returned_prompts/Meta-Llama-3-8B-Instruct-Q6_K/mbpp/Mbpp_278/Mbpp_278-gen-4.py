```
def count_first_elements(t):
    count = 0
    for elem in t:
        if isinstance(elem, tuple):
            break
        count += 1
    return count
```
The function `count_first_elements` takes a tuple as an argument and returns the number of elements that occur before the tuple element in the given tuple. It does this by iterating over the elements of the tuple until it finds a tuple. The count of elements before the tuple is then returned. 

For example, if we call `count_first_elements((1, 5, 7, (4, 6), 10))`, the function will return `3` because there are 3 elements before the tuple `(4, 6)` in the given tuple. 

This solution passes the given unit test: `assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3`. 

Note that this function does not consider nested tuples. If you want to consider nested tuples, you would need a more complex solution that recursively checks for tuples. 