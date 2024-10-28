```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```


Test:
```
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```


Explanation:
This problem is asking to create a function that takes a list of strings as input and returns a new list where each string in the input list is reversed. The unit test provided helps to clarify the expected output.

The solution uses a list comprehension to create a new list. For each string in the input list, it uses slicing with a step of -1 (`s[::-1]`) to reverse the string. The resulting list of reversed strings is then returned. The unit test checks that the function works correctly for a given list of strings.