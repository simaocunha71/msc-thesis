```
def remove_lowercase(s):
    return ''.join(c for c in s if not c.islower())
```


This function uses a generator expression to iterate over each character in the input string. The `islower()` method is used to check if a character is lowercase. If the character is not lowercase (i.e., it is uppercase or a non-alphabetic character), it is included in the resulting string. The `join()` method is used to concatenate the characters into a single string. 

For example, `remove_lowercase("PYTHon")` returns `'PYTH'` as expected. 

This function is case-sensitive, so it will remove both lowercase and title-case letters. If you want to remove only title-case letters, you can modify the condition in the generator expression to `c.istitle()` instead of `not c.islower()`. 

Please note that the problem statement doesn't specify what to do with title-case letters, but based on the unit test provided, it seems that they should be kept in the output. If you want to remove title-case letters as well, you can modify the condition to `c.isupper()` instead of `not c.islower()`. 
```python
def remove_lowercase(s):
    return ''.join(c for c in s if c.isupper())
``` 
This function will return `'PY'` for the input `'PYTHon'`. 
```python
def remove_lowercase(s):
    return ''.join(c for c in s if c.isupper() or not c.isalpha())
``` 
This function will return `'PYTH'` for the input `'PYTHon'`. It keeps uppercase letters and non-alphabetic characters, and removes lowercase letters. 
```python
def remove_lowercase(s):
    result = ''
    for c in s:
        if c.isupper():
            result += c
    return result
``` 
This function uses a for loop to iterate over each character in the input string. It checks if the character is uppercase using the `isupper()` method, and if it is, it adds it to the result string. The `result` string is then returned. 
```python
def remove_lowercase(s):
    return ''.join(filter(lambda c: c.isupper(), s))
``` 
This function uses the `filter()` function with a lambda function as the first argument. The lambda function takes a character `c` as input and returns `c` if `c` is uppercase, and `None` otherwise. The