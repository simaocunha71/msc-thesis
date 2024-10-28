```python
def sort_numbers(numbers: str) -> str:
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return ' '.join(sorted(numbers.split(), key=lambda x: num_dict[x]))

print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this solution, we first define a dictionary `num_dict` where the keys are the words from 'zero' to 'nine' and the values are their corresponding numbers. Then, we split the input string `numbers` by spaces into a list of words and sort that list using the values from `num_dict` as the key. Finally, we join the sorted list back into a string with spaces between the words and return it.

This way, the string is sorted from smallest to largest as per the word-number mapping in `num_dict`.
"""

# 