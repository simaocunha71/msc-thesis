remove_vowels = lambda text: ''.join(c for c in text if c not in 'aeiouAEIOU')

Here's some sample output to test your function:
```python
print(remove_vowels('')) # prints: ''
print(remove_vowels("abcdef\nghijklm")) # prints: 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # prints: 'bcdf'
print(remove_vowels('aaaaa')) # prints: ''
print(remove_vowels('aaBAA')) # prints: 'B'
print(remove_vowels('zbcd')) # prints: 'zbcd'
```

The lambda function is used to create an anonymous function that takes the `text` as an argument and returns the string without vowels. The `c for c in text if c not in 'aeiouAEIOU'` part of the code is a list comprehension that iterates through each character in the `text` and checks if it is not a vowel. If the character is not a vowel, it is added to the result string. The `''.join()` function is used to join all the characters in the result string together into a single string.

To test the function, you can use the `print()` function to print the output of the function for different inputs. The sample outputs provided above show how the function should behave for different inputs.

Here are some additional test cases you can try:
```python
print(remove_vowels('Hello, World!')) # prints: 'Hll, Wrld!'
print(remove_vowels('Python Programming')) # prints: 'Pythn Prgrmmng'
print(remove_vowels('123456789')) # prints: '123456789'
```

These test cases show how the function should behave for different types of input, including strings with digits, uppercase letters, and spaces.

Overall, the lambda function `remove_vowels` takes a string as an argument and returns a new string with all the vowels removed. This can be useful for text processing tasks where you