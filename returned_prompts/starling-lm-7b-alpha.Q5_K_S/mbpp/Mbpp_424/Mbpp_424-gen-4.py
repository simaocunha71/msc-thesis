"""
Here is the function to solve the problem:

```python
def extract_rear(tuple):
    return [i[-1] for i in tuple]
```

Explanation:
This function uses list comprehension to iterate through each string in the tuple and return the last element (index -1) of each string.
"""

# Python code to get last element of each string in tuple
def extract_rear(tuple):
    return [i[-1] for i in tuple]

# Driver program
print(extract_rear(('Mers', 'for', 'Vers')))
```
