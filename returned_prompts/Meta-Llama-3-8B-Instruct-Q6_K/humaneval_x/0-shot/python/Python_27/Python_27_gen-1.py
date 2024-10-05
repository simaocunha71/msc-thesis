You can solve this problem by iterating over each character in the string and using the `swapcase()` method of the string. Here is the Python code that does this:

```python
def flip_case(string: str) -> str:
    return string.swapcase()
```

The `swapcase()` method swaps the case of each character in the string. It converts uppercase characters to lowercase and vice versa. This is exactly what we need to solve the problem.

For example, if you call `flip_case('Hello')`, it will return `'hELLO'`, which is the desired output. The function works with any input string, not just 'Hello'. It will flip the case of all characters in the string.