To convert the number into the desired base, we can follow these steps:

1. Initialize a stack to store the digits of the number.
2. While the number is greater than 0, do the following:
   a. Calculate the remainder of the number divided by the base.
   b. Push the remainder onto the stack.
   c. Divide the number by the base.
3. While the stack is not empty, do the following:
   a. Pop the top element from the stack.
   b. Convert the popped element to a string and add it to the result.
4. Return the result.

Here's a Python implementation of the algorithm:

```python
def changeBase(x, base):
    result = ""
    while x > 0:
        result += str(x % base)
        x //= base
    return result[::-1]
```

This implementation initializes an empty string called `result` to store the final result. The while loop runs as long as `x` is greater than 0. Inside the loop, the remainder of `x` divided by `base` is appended to the `result` string. Then, `x` is divided by `base` to move on to the next digit. After the while loop, the `result` string is reversed using the `[::-1]` slicing syntax to obtain the correct order of digits. Finally, the reversed `result` string is returned.

You can use the `changeBase` function to convert a number to a different base. For example, `changeBase(8, 3)` returns `'22'`, `changeBase(8, 2)` returns `'1000'`, and `changeBase(7, 2)` returns `'111'`.

Note: The function `changeBase` provided above is a Python implementation. If you are using a different programming language, you may need to adapt the code accordingly.

Here's a Python implementation of the algorithm:

```python
def changeBase(x, base):
    result = ""
    while x > 0:
        result += str(x % base)
        x //= base
    return result[::-1]
```

