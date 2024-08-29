Here is a simple function to solve the problem:

```python
def change_date_format(date):
    return date[8:] + '-' + date[5:7] + '-' + date[:4]
```

This function splits the date string into three parts: the year, month, and day, and then reassembles the string in the desired format.

You can test the function with the provided assertion:

```python
print(change_date_format("2026-01-02"))  # prints: '02-01-2026'
```
"""


def change_date_format(date):
    return date[8:] + '-' + date[5:7] + '-' + date[:4]


print(change_date_format("2026-01-02"))  # prints: '02-01-2026'
<jupyter_output>
02-01-2026
<jupyter_text>
Q2:
<jupyter_code>
"""
