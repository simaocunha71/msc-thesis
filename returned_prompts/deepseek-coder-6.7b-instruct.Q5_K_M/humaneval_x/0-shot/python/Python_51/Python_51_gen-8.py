

def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([letter for letter in text if letter not in vowels])


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This function uses a list comprehension to create a new list that includes only the characters in the input text that are not vowels. The join() function is used to concatenate these characters into a new string.



```python
>>> remove_vowels('hello world')
'hll wrld'
```


```python
>>> remove_vowels('HELLO WORLD')
'HLL WRLD'
```


```python
>>> remove_vowels('AEIOUaeiou')
''
```
"""

# doctest.testmod() will run the tests and report any failures


def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([letter for letter in text if letter not in vowels])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```




























































































































































































































