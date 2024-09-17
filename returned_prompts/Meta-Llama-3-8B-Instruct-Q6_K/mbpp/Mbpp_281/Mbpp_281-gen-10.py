```
def all_unique(lst):
    return len(lst) == len(set(lst))
```


Here is how the function works:

- It takes a list as an argument.
- It compares the length of the list with the length of a set created from the list.
- In Python, a set is an unordered collection of unique elements. So, if the list contains duplicate elements, the set will have fewer elements than the list.
- The function returns True if the lengths are equal, which means all elements in the list are unique. Otherwise, it returns False.