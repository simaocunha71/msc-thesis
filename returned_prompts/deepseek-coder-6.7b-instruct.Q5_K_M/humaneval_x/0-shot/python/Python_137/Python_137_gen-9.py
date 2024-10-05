
def compare_one(a, b):
    if isinstance(a, str):
        if "," in a:
            a = float(a.replace(",", "."))
        else:
            a = float(a)
    if isinstance(b, str):
        if "," in b:
            b = float(b.replace(",", "."))
        else:
            b = float(b)

    if isinstance(a, float) or isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
    elif a > b:
        return a
    elif b > a:
        return b
    else:
        return None

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None

The function first checks if the inputs are strings, if true, it replaces the comma with a dot and converts the string to float. Then, it compares the inputs and returns the larger one. If the inputs are equal, it returns None.
"""
</code>
</pre>
</details>

## Problem 2

<details>
<summary>
Solve the problem
</summary>
<pre>
<code>
