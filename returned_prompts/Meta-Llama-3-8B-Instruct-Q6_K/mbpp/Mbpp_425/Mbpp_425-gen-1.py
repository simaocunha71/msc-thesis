```
def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count
```


This function iterates over each sublist in the given list, checks if the given element is present in the sublist, and increments a counter if it is. The counter is then returned as the count of sublists containing the given element. The provided unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` demonstrates the function's correctness.