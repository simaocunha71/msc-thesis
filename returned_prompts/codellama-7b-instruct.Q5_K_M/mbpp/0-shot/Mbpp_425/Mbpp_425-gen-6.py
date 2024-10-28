```
def count_element_in_list(list_to_check, element):
    count = 0
    for sublist in list_to_check:
        if element in sublist:
            count += 1
    return count
```
