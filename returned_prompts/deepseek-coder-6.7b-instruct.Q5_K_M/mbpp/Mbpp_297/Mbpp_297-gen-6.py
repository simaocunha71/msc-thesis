Here is the Python function:

```python
def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list
```

You can use the function like this:

```python
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
```

Output:

```
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```
"""

def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list

# Test the function
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
"""
