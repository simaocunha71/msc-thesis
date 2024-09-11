def replace_list(list1, list2):
    # concatenate the two lists together
    new_list = list1 + list2
    # remove the last element of the new list
    new_list = new_list[:-len(list2)]
    # return the new list
    return new_list

# test the function
print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])) # should return: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# test the function again
print(replace_list([1, 3, 5, 7, 9, 10],[1, 3, 5, 7, 9, 10])) # should return: [1, 3, 5, 7, 9, 1]






















"""
def replace_list(list1, list2):
    # check if the second list is longer than the first list
    if len(list2) > len(list1):
        # if true, then append the first list to the second list
        new_list = list2 + list1
    else:
        # if false, then append the second list to the first list
        new_list = list1 + list2
    # remove the last element of the new list
    new_list = new_list[:-len(list2)]
    # return the new list
    return new_list
"""


```


```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
