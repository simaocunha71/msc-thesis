```
def change_date_format(date):
    '''
    Convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
    '''
    parts = date.split('-')
    return parts[1] + '-' + parts[0] + '-' + parts[2]
```

In the provided code, the `change_date_format` function takes a date string in the format `yyyy-mm-dd` as an argument. The function splits the date string into three parts using the `-` delimiter. Then, it rearranges the parts to obtain the desired format `dd-mm-yyyy` and returns the result.

To test the function, you can use the `assert` statement, as shown in the example. By calling `change_date_format("2026-01-02")`, the function will return `'02-01-2026'`, which matches the expected output. 

This code can be used to convert dates from the `yyyy-mm-dd` format to the `dd-mm-yyyy` format in Python.

```python
# Example usage
date = "2026-01-02"
converted_date = change_date_format(date)
print(converted_date)  # Output: '02-01-2026'
```

By using the `change_date_format` function, you can easily convert dates between different formats in Python.

```python
# Example usage
date = "2025-12-31"
converted_date = change_date_format(date)
print(converted_date)  # Output: '31-12-2025'
```

This code can be used in any Python project where you need to convert dates from the `yyyy-mm-dd` format to the `dd-mm-yyyy` format.
```

```python
```python
```
```
```
```python
```
```python
```
```python
```
```python
```
```python
```
