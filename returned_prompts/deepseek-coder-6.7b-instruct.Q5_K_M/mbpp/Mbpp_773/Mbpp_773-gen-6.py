Here is the Python solution to the problem:

```python
def occurance_substring(s, sub):
    pos = s.find(sub)
    if pos != -1:
        return (sub, pos, pos+len(sub))
    else:
        return None

print(occurance_substring('python programming, python language','python'))
```

In the above code, the `find()` method is used to find the first occurrence of the specified value. The `find()` method returns -1 if the value is not found. The position of the occurrence is returned along with the matched string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
