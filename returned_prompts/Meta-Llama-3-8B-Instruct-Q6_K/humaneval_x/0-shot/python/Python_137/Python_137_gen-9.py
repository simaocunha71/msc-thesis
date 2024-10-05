
Here is the Python code for the problem:
```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, (int, float)):
        a = float(a.replace(",", ""))
    elif isinstance(b, str