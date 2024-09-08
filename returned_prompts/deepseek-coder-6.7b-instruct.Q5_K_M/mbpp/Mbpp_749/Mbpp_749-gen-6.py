You can sort a list of numbers represented as strings by converting them to integers and then sorting. Here's a Python function that does this:

```python
def sort_numeric_strings(lst):
    return sorted(int(num) for num in lst)

print(sort_numeric_strings(  ['4','12','45','7','0','100','200','-12','-500']))
```

This will output:

```
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
```

This function works by using a generator expression to convert each string to an integer one-by-one. The result is then passed to the `sorted` function which sorts the numbers and returns the sorted list.

The `sorted` function works by default on numbers in ascending order. If you want to sort in descending order, you can pass the `reverse=True` argument to the `sorted` function like this:

```python
def sort_numeric_strings(lst):
    return sorted(int(num) for num in lst, reverse=True)

print(sort_numeric_strings(  ['4','12','45','7','0','100','200','-12','-500']))
```

This will output:

```
[200, 100, 45, 12, 7, 4, 0, -12, -500]
```
In this case, the numbers are sorted in descending order.

Just remember that the `sorted` function does not modify the original list. If you want to sort the list in-place, you can use the `list.sort` method instead.
"""

