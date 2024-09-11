```
def change_date_format(date):
    return '-'.join(date.split('-')[::-1])
```

Explanation:
The task is to convert a date in the format yyyy-mm-dd to dd-mm-yyyy. The provided function, `change_date_format`, takes a date string as input and uses the `split` method to split the date string at every hyphen. The `[::-1]` part of the code is used to reverse the order of the date string. This means that the year comes first, followed by the month, and then the day. Finally, the `join` method is used to concatenate the reversed date string back together, with hyphens in between each part. This results in a date string in the format dd-mm-yyyy, as required. The function is tested with the example input of `"2026-01-02"`, and it correctly returns `'02-01-2026'`.

To use the function, you can simply call it with a date string in the format yyyy-mm-dd. For example:
```python
result = change_date_format("2022-03-15")
print(result)  # Output: '15-03-2022'
```

In this example, the date string `"2022-03-15"` is passed to the `change_date_format` function. The function correctly converts the date to the format `'15-03-2022'`, and the result is printed to the console.

Overall, the `change_date_format` function provides a simple and efficient solution to convert a date in the format yyyy-mm-dd to dd-mm-yyyy.

```python
def change_date_format(date):
    return '-'.join(date.split('-')[::-1])
```

This function takes a date string as input and splits it at every hyphen using the `split` method. The `[::-1]` part of the code is used to reverse the order of the date string, so that the year comes first, followed