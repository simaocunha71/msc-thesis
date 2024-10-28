```python
def unique(l):
    return sorted(set(l))
```


Explanation:
This problem is asking you to create a function that takes a list as input and returns a new list with the same elements, but with duplicates removed and in sorted order.

The solution is to use the built-in `set` function to remove duplicates, and then use the `sorted` function to sort the resulting set. The `set` function returns a set object, which is an unordered collection of unique elements. The `sorted` function returns a new sorted list from the elements of any sequence.

Here's the code in Python:
```python
def unique(l):
    return sorted(set(l))
```
This function works by first converting the input list `l` to a set using the `set` function. This removes any duplicate elements from the list. Then, it sorts the resulting set using the `sorted` function, and returns the sorted list.

For example, if you call the function with the input list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`, it will return the list `[0, 2, 3, 5, 9, 123]`. This is because the set of the input list is `{0, 2, 3, 5, 9, 123}`, and the sorted list of this set is `[0, 2, 3, 5, 9, 123]`.