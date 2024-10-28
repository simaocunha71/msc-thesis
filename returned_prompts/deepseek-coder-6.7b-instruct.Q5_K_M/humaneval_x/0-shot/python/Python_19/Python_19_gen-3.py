```python
def sort_numbers(numbers: str) -> str:
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    numbers_split = numbers.split()
    numbers_sorted = sorted(numbers_split, key=lambda x: num_dict[x])
    return ' '.join(numbers_sorted)
```

This function works by first creating a dictionary that maps the string representation of numbers to their numerical values. It then splits the input string into a list of numbers represented as strings. It sorts this list using the `sorted` function and a key that uses the dictionary to map strings to their numerical values. Finally, it joins the sorted list into a single string with spaces between the numbers and returns this string.



```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This function works by first creating a dictionary that maps the string representation of numbers to their numerical values. It then splits the input string into a list of numbers represented as strings. It sorts this list using the `sorted` function and a key that uses the dictionary to map strings to their numerical values. Finally, it joins the sorted list into a single string with spaces between the numbers and returns this string.



```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This function works by first creating a dictionary that maps the string representation of numbers to their numerical values. It then splits the input string into a list of numbers represented as strings. It sorts this list using the `sorted` function and a key that uses the dictionary to map strings to their numerical values. Finally, it joins the sorted list into a single string with spaces between the numbers and returns this string.



```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This function works by first creating a dictionary that maps the string representation of numbers to their numerical values. It then splits the input string into a list of numbers represented as strings. It sorts this