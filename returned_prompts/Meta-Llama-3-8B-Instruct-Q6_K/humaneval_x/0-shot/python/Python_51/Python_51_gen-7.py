```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
```
This function works by iterating over each character in the input string. If the character is not a vowel (i.e., it is not in the string 'aeiouAEIOU'), it is added to the result string. The function then returns the result string. The function also handles uppercase vowels by including 'AEIOU' in the string of vowels. 

This function works with strings that contain newline characters, as shown in the example where the input string is "abcdef\nghijklm". It also works correctly with strings that contain only vowels, as shown in the example where the input string is 'aaaaa'. 

Finally, this function correctly handles strings that contain a mix of vowels and non-vowels, as shown in the example where the input string is 'aaBAA'. It also correctly handles strings that contain no vowels, as shown in the example where the input string is 'zbcd'. 