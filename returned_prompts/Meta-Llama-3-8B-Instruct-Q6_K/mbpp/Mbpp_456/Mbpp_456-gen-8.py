```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```
The problem is asking you to write a function that takes a list of strings as input and returns a new list where each string in the original list is reversed.

The unit test provided suggests that the input list is a list of strings, and the function should return a list of strings where each string is the reverse of the corresponding string in the input list.

Here's how you can solve this problem:

1. Use a list comprehension to iterate over each string in the input list.
2. Use slicing to reverse each string. In Python, you can use slicing with a step of -1 to reverse a string. For example, the string "hello" becomes "olleh" with `s[::-1]`.
3. Return the list of reversed strings.

Here's the solution in Python:
```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```
This function uses a list comprehension to iterate over each string in the input list `lst`. For each string `s`, it uses slicing with a step of -1 to reverse the string, and returns a new list containing the reversed strings. The unit test provided suggests that this function should return the expected output for the input list `['Red', 'Green', 'Blue', 'White', 'Black']`.