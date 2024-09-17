The problem asks to write a function that takes a list of integers as input and returns a single integer formed by concatenating the input integers. For example, if the input is [11, 33, 50], the output should be 113350.

Here's a Python solution for the problem:
```
def multiple_to_single(lst):
    return int(''.join(map(str, lst)))
```
This function works by first converting each integer in the list to a string using the `map` function. Then, it joins these strings together into a single string using the `join` method. Finally, it converts this string back to an integer using the `int` function.

The unit test `assert multiple_to_single([11, 33, 50])==113350` ensures that the function works correctly. It checks that the output of the function is equal to 113350 when the input is [11, 33, 50]. If the function is implemented correctly, this test should pass. If the function is implemented incorrectly, this test will fail, indicating that there is a bug in the function.