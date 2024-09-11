Here's a Python function that can be used to find the first digit of a given number:

```python
def first_Digit(n):
    n = str(n)
    return int(n[0])
```

Explanation:
The function first_Digit takes a number as input and converts it to a string using the str() function. Then, it uses the indexing operator [0] to access the first character of the string. Since strings are indexed starting from 0, the first character is at index 0. The function then converts the first character back to an integer using the int() function and returns it as the result.

For example, if we call first_Digit(123), it will return 1, as the first digit of 123 is 1.

It's important to note that this function assumes the given number is a positive integer. If the input is not a positive integer, the function may not produce the expected result.

```python
def first_Digit(n):
    n = str(n)
    return int(n[0])
```

To use the function, simply call it with the desired number as the argument. For example, to find the first digit of the number 123, you can call `first_Digit(123)`, which will return 1.

Here are some additional examples of using the function:

```python
print(first_Digit(456))  # Output: 4
print(first_Digit(789))  # Output: 7
print(first_Digit(1011))  # Output: 1
```

By using the function `first_Digit`, you can easily find the first digit of any positive integer in Python.

```python
def first_Digit(n):
    n = str(n)
    return int(n[0])
```

I hope this explanation helps you understand how the function works and how to use it in your Python code. Let me know if you have any more questions!
```

```
  
  
