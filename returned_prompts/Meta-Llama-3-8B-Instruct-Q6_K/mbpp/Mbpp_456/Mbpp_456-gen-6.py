```
def reverse_string_list(input_list):
    return [s[::-1] for s in input_list]
``` 





This function uses a list comprehension to iterate over each string in the input list, and for each string, it uses slicing with a step of -1 (`s[::-1]`) to reverse the string. The resulting list of reversed strings is then returned. 





The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` demonstrates that the function works correctly.