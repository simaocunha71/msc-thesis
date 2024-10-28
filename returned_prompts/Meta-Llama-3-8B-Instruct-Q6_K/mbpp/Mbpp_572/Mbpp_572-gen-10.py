```
def two_unique_nums(lst):
    unique_nums = set(lst)
    return sorted(list(unique_nums))
```
This function takes a list of numbers as input, converts it to a set (which removes duplicates) and then converts it back to a list. It then sorts the list and returns it.

The unit test `assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]` helps to understand the problem better. It suggests that we need to remove duplicate numbers from a single list, not from multiple lists. 

So, this function can be used to remove duplicate numbers from a single list. If you need to remove duplicate numbers from multiple lists, you would need a different function that takes a list of lists as input and returns a list of unique numbers from all the lists. 

Here is a function that does that:
```
def unique_nums_from_lists(lists):
    unique_nums = set()
    for lst in lists:
        unique_nums.update(set(lst))
    return sorted(list(unique_nums))
```
This function takes a list of lists as input, iterates over the lists, converts each list to a set and updates the main set with the unique numbers from each list. Finally, it converts the set to a list, sorts it and returns it. 

For example, if you have two lists `[1,2,3,2,3,4,5]` and `[6,7,8,9,10]`, you can use this function to get a list of unique numbers from both lists: `unique_nums_from_lists([[1,2,3,2,3,4,5], [6,7,8,9,10]])` would return `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. 