```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])
```


This function uses a list comprehension to create a new list that includes only the characters from the input string that are not vowels. It then uses the `join` method to concatenate these characters into a new string, which is returned by the function.

For example, if you call `remove_vowels('abcdef')`, the function will return `'bcdf'`. If you call `remove_vowels('aaaaa')`, the function will return an empty string, because all the characters in the input string are vowels. If you call `remove_vowels('aaBAA')`, the function will return `'B'`, because the only non-vowel character in the input string is the letter `'B'`. If you call `remove_vowels('zbcd')`, the function will return `'zbcd'`, because all the characters in the input string are non-vowels.

The function handles newline characters and spaces correctly, as shown by the test cases. It also correctly handles uppercase and lowercase vowels. For example, if you call `remove_vowels('AaB')`, the function will return `'B'`, because the only non-vowel character in the input string is the letter `'B'`. If you call `remove_vowels('aeiou')`, the function will return an empty string, because all the characters in the input string are vowels. If you call `remove_vowels('bcdf')`, the function will return `'bcdf'`, because all the characters in the input string are non-vowels.