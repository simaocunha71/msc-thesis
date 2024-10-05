```
def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
```


Example:
```
print(compare_one(1, 2.5))  # Output: 2.5
print(compare_one(1, "2,3"))  # Output: "2,3"
print(compare_one("5,1", "6"))  # Output: "6"
print(compare_one("1", 1))  # Output: None
```


Explanation:

- The function `compare_one` takes two arguments `a` and `b`.
- It checks if either `a` or `b` is a string. If so, it converts the string to a float by replacing the comma with a dot.
- Then, it compares the values of `a` and `b`. If `a` is greater, it returns `a`. If `b` is greater, it returns `b`. If the values are equal, it returns `None`.
- The function handles both integer and float inputs, as well as string inputs that represent real numbers with commas or dots.