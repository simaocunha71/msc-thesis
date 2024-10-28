```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```
The problem is asking to write a function that takes a list of strings as input and returns a new list with each string reversed. 

The unit test provided, `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`, helps to clarify the problem.

The solution uses a list comprehension to iterate over each string in the input list. For each string, it uses slicing with a step of -1 (`s[::-1]`) to reverse the string. The resulting list of reversed strings is then returned. 

For example, if the input is `['Red', 'Green', 'Blue', 'White', 'Black']`, the function will return `['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`. 