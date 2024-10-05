```
def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(",", ".").replace(",", ".")
        a = float(a)
    if isinstance(b, str):
        b = b.replace(",", ".").replace(",", ".")
        b = float(b)
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
```


Example inputs/outputs:

- compare_one(1, 2.5) ➞ 2.5
- compare_one(1, "2,3") ➞ "2,3"
- compare_one("5,1", "6") ➞ "6"
- compare_one("1", 1) ➞ None
- compare_one("1", "2") ➞ "2"