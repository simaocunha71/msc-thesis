

def change_base(x: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]
```

This function takes an integer `x` and a base `b` as inputs. It uses recursion to convert the number `x` to its string representation in the given base `b`. The function first checks if `x` is less than `b`, in which case it returns the corresponding digit from the `digits` string. If `x` is greater than or equal to `b`, it recursively calls itself with `x` divided by `b` and appends the digit corresponding to the remainder of `x` divided by `b`. Finally, the function returns the concatenated string of digits.

For example, when `change_base(8, 3)` is called, it recursively converts 8 to its string representation in base 3. The result is '22', which is returned by the function.

The function can handle bases less than 10, as the `digits` string includes all the necessary digits for bases up to 36.

Here are some test cases for the function:

```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

These test cases demonstrate the correctness of the `change_base` function.

```

```