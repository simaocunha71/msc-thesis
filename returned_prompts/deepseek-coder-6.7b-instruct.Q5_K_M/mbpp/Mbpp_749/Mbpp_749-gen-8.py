Here is a Python solution using the built-in sort() function:

```python
def sort_numeric_strings(lst):
    return sorted(lst, key=int)

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

This will return the expected output: `[-500, -12, 0, 4, 7, 12, 45, 100, 200]`. The key parameter is set to int, so the list is sorted as integers, not strings.

If you prefer to modify the original list, you can use the sort() function directly on the list:

```python
def sort_numeric_strings(lst):
    lst.sort(key=int)
    return lst

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

This will also return the expected output: `[-500, -12, 0, 4, 7, 12, 45, 100, 200]`.

In both cases, the sort() function is used with the key parameter set to int, so the list is sorted as integers, not strings.

Please note that the sort() function sorts the list in-place, meaning that it modifies the original list. If you want to keep the original list unchanged, you should use the sorted() function instead.

Also, it's important to note that the sort() and sorted() functions are case-sensitive. If you want to sort the numbers in a case-insensitive way, you should add a key function that converts the strings to lowercase or uppercase before sorting.

Lastly, these solutions assume that the input list contains only numeric strings. If the list might contain non-numeric strings, you should add error handling to handle these cases.
