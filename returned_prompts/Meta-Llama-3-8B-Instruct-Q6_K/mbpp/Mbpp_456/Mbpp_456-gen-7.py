```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```





The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` helps to understand the problem. It's asking to reverse each string in the given list of string values. 

In Python, you can achieve this by using list comprehension and slicing. The slicing `s[::-1]` returns a reversed copy of the string `s`. This is used to reverse each string in the list. The result is a new list with the reversed strings. 

Here's the solution:

```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```



This function takes a list of strings as input, and returns a new list with the same strings but in reverse order. For example, if the input is `['Red', 'Green', 'Blue']`, the output will be `['deR', 'neerG', 'eulB']`. 

The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` ensures that the function works correctly. It checks if the output of the function is equal to the expected output. If the output is not as expected, the test will fail, indicating that the function is not working correctly. 

In this case, the test passes, which means the function is working correctly. It correctly reverses each string in the input list and returns the result as a new list. 