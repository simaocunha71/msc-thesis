```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
``` 

The function `reverse_string_list` takes a list of strings as input and returns a new list with each string reversed. It uses a list comprehension to iterate over each string in the input list and reverse it using slicing (`s[::-1]`). The `[::-1]` slice means "start at the end of the string and end at position 0, move with the step -1". This effectively reverses the string. The reversed strings are then collected in a new list, which is returned by the function. 

For example, if we call `reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])`, it will return `['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`. 

The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` ensures that the function works as expected.  It checks that the output of the function is equal to the expected output. If the function is correct, the unit test will pass; otherwise, it will fail.  This helps to ensure that the function behaves correctly for different inputs. 