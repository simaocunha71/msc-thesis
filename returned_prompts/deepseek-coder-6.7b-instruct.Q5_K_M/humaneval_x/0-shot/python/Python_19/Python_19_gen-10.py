Here is the Python solution for the problem. 

```python
def sort_numbers(numbers: str) -> str:
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: num_dict[x])
    return ' '.join(numbers_list)
```

In this solution, we first define a dictionary where keys are the names of numbers from 'zero' to 'nine' and values are their corresponding integer values. 

Then, we split the input string `numbers` into a list of words. 

Then, we sort the list `numbers_list` using the dictionary `num_dict` as a key to sort the words. The key function `lambda x: num_dict[x]` is used to specify that the sorting should be done based on the integer values of the words, not the words themselves.

Finally, we join the sorted list `numbers_list` into a string with a space as the delimiter and return it.

Note: The sorting of the list is in ascending order.

Testing the function with the provided example:

```python
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This function works by translating the words to numbers, sorting the numbers, and then translating them back to words. It's important to note that the words 'one', 'three', and 'five' are sorted in ascending order.

Also, it's worth mentioning that the function does not handle cases where the input string contains words that are not valid numbers. If such a case is encountered, it will raise a KeyError.

The time complexity of the function is O(nlogn) due to the sort operation. The space complexity is O(n) as we create a list from the input string.
```


































