```
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            break
        count += 1
    return count
```
The function `count_first_elements` iterates over the elements of the given tuple `t`. It increments the `count` variable for each element until it encounters a tuple. The function then returns the `count` value. The unit test `assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3` ensures that the function works correctly.