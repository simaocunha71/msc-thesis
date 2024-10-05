
Here's a solution in Python:

```python
def string_xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == '0' and b[i] == '0':
            result += '0'
        elif a[i] == '0' and b[i] == '1':
            result += '1'
        elif a[i] == '1' and b[i] == '0':
            result += '1'
        else:
            result += '0'
    return result
```

This function takes two binary strings `a` and `b` as input and performs bitwise XOR operation on them. It initializes an empty string `result` to store the result of the XOR operation. Then, it iterates over each character in the input strings using a `for` loop.

Inside the loop, it checks the corresponding characters in `a` and `b`. If both characters are '0', it appends '0' to the `result` string. If one character is '0' and the other is '1', it appends '1' to the `result` string. If both characters are '1', it appends '0' to the `result` string. If one character is '0' and the other is '0', it appends '1' to the `