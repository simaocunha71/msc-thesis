```
def two_unique_nums(lst):
    return list(set([num for num in lst if lst.count(num) == 1]))
```
This function will return a list of unique numbers from the given list. It uses a list comprehension to create a new list that includes only the numbers that appear only once in the original list. The set function is used to remove duplicates from the new list.

The unit test `assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]` shows that the function should return a list of unique numbers from the given list.

For example, if we call the function with the list `[1,2,3,2,3,4,5]`, it will return the list `[1, 4, 5]`, which are the unique numbers from the original list.