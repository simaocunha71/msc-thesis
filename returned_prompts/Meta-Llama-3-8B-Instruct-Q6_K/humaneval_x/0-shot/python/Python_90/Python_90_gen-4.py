```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]
```



The function first checks if the list has less than 2 elements. If it does, it returns None because there is no 2nd smallest element. It then removes duplicates from the list by converting it to a set and then back to a list. If the resulting list has less than 2 elements, it means that the list had less than 2 unique elements, so the function returns None. Otherwise, it returns the 2nd smallest element by indexing the sorted list at 1. 

Note that this function does not modify the original list. It also does not handle the case where the list contains non-integer elements. For a more robust solution, you might want to add error checking to handle these cases. 

Here is the code:

```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(set([x for x in lst if isinstance(x, int)]))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]
```



This version of the function uses a list comprehension to filter out non-integer elements from the list. It also checks the type of each element in the list before adding it to the set and the sorted list. This way, the function will not fail if the list contains non-integer elements. 

However, this function will still return None if the list contains non-integer elements and has less than 2 integer elements. If you want to handle this case differently, you will need to add additional error checking code. 

Here is an example of how you might do this:

```
def next_smallest(lst):
    if len([x for x in lst if isinstance(x, int)]) < 2:
        return None
    sorted_lst = sorted(set([x for x in lst if isinstance(x, int)]))
    return sorted_lst[1]
```



This version of the function will return the 2nd smallest integer in the list, or None if the list contains less than 2 integers. It will not return None if the list contains non-integer elements, even if it has less than 2 integer elements. 

You can further modify this function to fit your specific requirements. For example,