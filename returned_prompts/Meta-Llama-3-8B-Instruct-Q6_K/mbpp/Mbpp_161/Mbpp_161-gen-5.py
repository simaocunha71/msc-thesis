```
def remove_elements(lst1, lst2):
    return [value for value in lst1 if value not in lst2]
```


The function `remove_elements` takes two lists `lst1` and `lst2` as input. It uses a list comprehension to create a new list that includes all elements from `lst1` that are not present in `lst2`. The condition `value not in lst2` is used to filter out elements from `lst1` that are present in `lst2`. The resulting list is then returned.

For example, if we call `remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])`, the function will return `[1, 3, 5, 7, 9, 10]`, which are the elements from the first list that are not present in the second list. This is confirmed by the provided unit test.