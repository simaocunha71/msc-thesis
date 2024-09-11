"""
def sort_numeric_strings(lst):
    return sorted(lst, key=int)
"""

In Python, built-in function sorted() can be used to sort a given list. The sorted() function uses the key parameter to specify a function of one argument that is used to extract a comparison key from each list element. Here, the key parameter is set to int to convert each string to a number and perform a numerical comparison. The returned result is a new sorted list of strings.

To test the function, you can use the Python built-in function assert to verify the result. The assert statement checks if the condition is true and raises an AssertionError if the condition is false. In this case, the condition is whether the result of sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']) equals to [-500, -12, 0, 4, 7, 12, 45, 100, 200]. If the condition is true, the program will not raise an error; otherwise, an error will be raised.

In Python, the minus sign (-) is used to denote a negative number.

Here is an example to use the function:

```python
def sort_numeric_strings(lst):
    return sorted(lst, key=int)

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))
```

This will return: [-500, -12, 0, 4, 7, 12, 45, 100, 200].

"""

# Your code goes here
def sort_numeric_strings(lst):
    return sorted(lst, key=int)

# Test the function
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
print(sort