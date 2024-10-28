```
def count_element_in_list(list_of_lists, element):
    count = 0
    for sublist in list_of_lists:
        if element in sublist:
            count += 1
    return count
```


The function `count_element_in_list` takes a list of lists and an element as input. It iterates over each sublist in the list of lists and checks if the element is present in the sublist. If the element is found, it increments a counter. Finally, it returns the count of sublists containing the element.

For example, if we have the list of lists `[[1, 3], [5, 7], [1, 11], [1, 15, 7]]` and we want to count the number of sublists containing the element `1`, the function will return `3` because `1` is present in three sublists. This is confirmed by the unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3`. 