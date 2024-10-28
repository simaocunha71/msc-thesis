```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, str):
        a = float(a.replace(",", ""))
        b = float(b.replace(",", ""))
    elif isinstance(a, str):
        a = float(a.replace(",", ""))
    elif isinstance(b, str):
        b = float(b.replace(",", ""))
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
```


The provided function, compare_one, takes two arguments, a and b, and compares them based on their type. If both arguments are strings, it converts them to float values by removing the commas. If only one argument is a string, it converts that one to a float. Finally, it compares the values and returns the larger one if they are not equal. If they are equal, it returns None.