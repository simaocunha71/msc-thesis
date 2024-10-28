
Here is a step-by-step guide on how to write a function that removes vowels from a string:

1. Define a function called `remove_vowels` that takes a single argument called `text`. This function will return a string without vowels.

2. In the function, use a list of vowels (`vowels = ['a', 'e', 'i', 'o', 'u']`) to iterate over each vowel in the input string.

3. Use the `replace()` method to replace each vowel in the string with an empty string (`''`). This will remove the vowel from the string.

4. Return the modified string.

Here's the code that implements these steps:

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        text = text.replace(vowel, '')
    return text
```

You can test the function using the following code:

```python
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
