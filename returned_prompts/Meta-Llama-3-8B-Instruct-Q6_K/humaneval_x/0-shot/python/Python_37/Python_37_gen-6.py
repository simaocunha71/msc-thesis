The solution to this problem can be found in the following code:

```python
def sort_even(l: list):
    even = sorted([x for x in l[::2]])
    return [x if i % 2 == 0 else x for i, x in enumerate(l)]
```

This function uses list comprehension to create two lists. The first list `even` contains the elements of the original list at even indices, sorted. The second list is created by iterating over the original list and replacing elements at even indices with their sorted values, and keeping elements at odd indices unchanged. The resulting list is then returned. The time complexity of this function is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n) as we create a new list with the same length as the input list. 