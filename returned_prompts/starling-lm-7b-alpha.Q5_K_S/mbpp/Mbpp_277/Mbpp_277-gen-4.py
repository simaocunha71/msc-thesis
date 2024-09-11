```python
def dict_filter(dictionary,n):
    return {key:value for key,value in dictionary.items() if value>=n}
```

In the function above, we use a dictionary comprehension to create a new dictionary that only includes entries with values greater than or equal to n. 

To test the function, we pass in the dictionary {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190} and the integer 