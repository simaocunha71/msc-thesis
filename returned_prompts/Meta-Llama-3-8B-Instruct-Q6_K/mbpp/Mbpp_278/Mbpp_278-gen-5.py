```
def count_first_elements(t):
    count = 0
    for i, element in enumerate(t):
        if isinstance(element, tuple):
            break
        count += 1
    return count
```


This function iterates over the given tuple and counts the number of elements before the first tuple element. When it encounters the first tuple element, it breaks the loop and returns the count. The unit test `assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3` ensures that the function is working correctly.