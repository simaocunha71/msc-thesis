Here is the Python function for the problem:

```python
def division_elements(t1, t2):
    return tuple(x // y for x, y in zip(t1, t2))
```

Test the function:

```python
print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))
```

This will output:

```
(2, 2, 2, 3)
```

Explanation:
The function `division_elements` takes two tuples `t1` and `t2` as inputs. It uses the `zip` function to pair up corresponding elements of both tuples. Then, it uses a tuple comprehension to perform division element-wise. The `//` operator performs integer division, which discards the fraction part. The result is a new tuple which is returned by the function.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
