```
def count_element_in_list(lst, element):
    count = 0
    for sublst in lst:
        if element in sublst:
            count += 1
    return count
```


The function `count_element_in_list` takes a list of lists `lst` and an element `element` as input. It iterates over each sublist in `lst` and checks if `element` is present in the sublist. If `element` is found in a sublist, it increments the `count` variable. Finally, it returns the total count of sublists containing `element`. The unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` ensures that the function works correctly. For example, the output `3` indicates that three sublists contain the element `1`.