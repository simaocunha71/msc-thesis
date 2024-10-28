Here is a possible Python solution for the problem:

```python
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 0 to 9.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_sorted = sorted(numbers.split(), key=lambda x: num_dict[x])
    return ' '.join(numbers_sorted)
```

This function works by first creating a dictionary that maps the words to their corresponding numbers. Then it splits the input string into a list of words, sorts the list based on the corresponding numbers from the dictionary, and then joins the sorted list back together into a string.

Please note that this function assumes that the input string is always valid, i.e., it contains only words from the dictionary and spaces between words. If this is not the case, you would need to add some error checking to handle invalid inputs.
