Here is the Python code which uses a dictionary to map the string numbers to actual numbers and then sorts them.

```python
def sort_numbers(numbers: str) -> str:
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: num_dict[x])
    return ' '.join(numbers_list)
```

Here is a step by step explanation of the code:

1. We first create a dictionary where keys are the numbers in words and values are the numbers in digits.
2. We split the input string into a list of words.
3. We sort the list of words based on the numbers in digits using the sort function and a lambda function to specify that we want to sort by the values in the dictionary.
4. Finally, we join the sorted list into a string with spaces in between the words and return it.

This solution assumes that the input string will always be in the correct format (i.e., will contain only valid words). If the input string might contain invalid words, you should add error checking to handle these cases.

Testing the code with your example:

```python
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This will output the string 'one three five' as expected.
"""

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




