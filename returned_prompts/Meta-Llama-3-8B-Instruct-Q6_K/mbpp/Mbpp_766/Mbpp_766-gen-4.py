```
def pair_wise(lst):
    return [(a, b) for a, b in zip(lst, lst[1:])]
```


The function pair_wise takes a list as an argument and returns a list of tuples, where each tuple contains a pair of consecutive items from the input list. It uses list comprehension and the built-in function zip to achieve this. 

The zip function takes two lists as arguments and returns an iterator of tuples, where the first item in each tuple is from the first list and the second item is from the second list. In this case, we use lst and lst[1:] as the two lists, which means the first item in each tuple will be from the original list, and the second item will be from the list shifted one position to the right. 

This function works as expected, as shown in the unit test. For example, if the input list is [1,1,2,3,3,4,4,5], the function will return [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]. 

The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate over the list once. The space complexity is also O(n), because it needs to store all the pairs of consecutive items in the output list. 

Note that this function does not handle the case where the input list is empty. If you want to handle this case, you can add a simple check at the beginning of the function. For example, you can return an empty list if the input list is empty. 

Here is the modified function:

```
def pair_wise(lst):
    if not lst:
        return []
    return [(a, b) for a, b in zip(lst, lst[1:])]
``` 














