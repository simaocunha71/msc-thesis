```python
def unique(lst):
    return sorted(set(lst))
```


Explanation:
- `set(lst)` removes duplicates from the list by converting it to a set (which automatically removes duplicates) and then converting it back to a list.
- `sorted(set(lst))` sorts the resulting list in ascending order. 

For example, if you run `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])`, it will return `[0, 2, 3, 5, 9, 123]`. 

This function assumes that the input is a list of elements that can be compared using the `<` operator, such as integers or strings. If the input can contain other types of elements, you may need to modify the function accordingly.