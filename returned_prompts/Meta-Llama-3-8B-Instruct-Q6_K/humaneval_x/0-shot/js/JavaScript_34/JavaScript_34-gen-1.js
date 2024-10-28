Here is the Python solution for the problem:

```Python
def unique(l):
    return sorted(set(l))

print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This function works by converting the list to a set, which automatically removes duplicates, and then converting the set back to a list and sorting it. The result is a list of unique elements in sorted order. The output of this function for the given input is `[0, 2, 3, 5, 9, 123]`. 

If you want to keep the original order of the elements, you can use a dictionary to keep track of the elements you've seen so far:

```Python
def unique(l):
    seen = {}
    return [x for x in l if not (x in seen or seen.__setitem__(x, 1))]

print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This function iterates over the list and for each element, it checks if the element is already in the `seen` dictionary. If it is not, it adds the element to the `seen` dictionary and includes it in the output list. The output of this function for the given input is also `[0, 2, 3, 5, 9, 123]`. 

The time complexity of both functions is O(n), where n is the length of the input list. The space complexity of the first function is O(n) and the space complexity of the second function is O(min(n, m)), where m is the number of unique elements in the list. 