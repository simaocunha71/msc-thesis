```
def ascii_value(char):
    return ord(char)
```


The function `ascii_value` takes a character as input and returns its ASCII value. The built-in Python function `ord` is used to get the ASCII value of a character. For example, `ord('A')` returns `65`. 

The unit test `assert ascii_value('A')==65` ensures that the function works correctly for the character 'A'. 

This function can be used with any character, not just uppercase letters. For example, `ascii_value('a')` would return `97`, the ASCII value of the lowercase letter 'a'. 
```python
print(ascii_value('A')) # Output: 65
print(ascii_value('a')) # Output: 97
```


This function can be used in a variety of applications, such as data processing, text analysis, or encryption, where the ASCII value of characters is necessary. For example, it can be used to convert characters to their corresponding ASCII values, or to filter out non-ASCII characters. 
```python
char = 'A'
ascii_value = ord(char)
print(ascii_value)  # Output: 65
```


Note that the `ord` function returns the Unicode code point for a one-character string. If the input is not a one-character string, it will raise a `TypeError`. For example, `ord('Hello')` would raise a `TypeError`. 
```python
char = 'Hello'
try:
    ascii_value = ord(char)
except TypeError:
    print("Input is not a one-character string.")
```


In this case, you would need to modify the function to handle multi-character strings. For example, you could iterate over the characters in the string and calculate their ASCII values separately. 
```python
def ascii_values(string):
    return [ord(char) for char in string]

print(ascii_values('Hello'))  # Output: [72, 101, 108, 108, 111]
```


This modified function would return a list of ASCII values for each character in the input string. 
```python
char = 'Hello'
ascii_values = [ord(char) for char in char]
print(ascii_values)  # Output: [72, 101, 108, 108, 111]
```


This function can be used to get the ASCII values of a string, which can be useful in a variety of applications, such as data processing, text analysis, or encryption