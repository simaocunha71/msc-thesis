```python
def sort_numbers(numbers: str) -> str:
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list = numbers.split()
    num_list.sort(key=lambda x: num_dict[x])
    return ' '.join(num_list)
```

Here, we first define a dictionary to map the string numbers to their corresponding numbers. Then, we split the input string into a list of words. We then sort this list using the values from the dictionary as the key to sort by the numerical value of the words. Finally, we join the sorted list back into a string with spaces in between each word and return this string.

This solution assumes that the input string will always be a space-delimited string of valid words. It also assumes that the input string will not contain any other characters than the words and spaces.

Note: The sort() method sorts the list in-place, meaning that it changes the original list. The join() method combines all the words in the list into a single string with spaces in between each word.

```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
"""
```

### Python Code:
```python
def sort_numbers(numbers: str) -> str:
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list = numbers.split()
    num_list.sort(key=lambda x: num_dict[x])
    return ' '.join(num_list)
```

```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This function works by first creating a dictionary that maps the string representations of numbers to their integer counterparts. It then splits the input string into a list of words. This list is then sorted in ascending