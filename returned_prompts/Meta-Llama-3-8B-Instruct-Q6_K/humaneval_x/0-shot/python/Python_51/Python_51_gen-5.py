```
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
```


This function takes a string as input, iterates over each character in the string, and checks if the character is a vowel. If it is not a vowel, it adds the character to the result string. Finally, it returns the result string. The function handles both lowercase and uppercase vowels. The function also preserves the original case of the characters in the input string. The time complexity of this function is O(n), where n is the length of the input string, because it iterates over each character in the string once. The space complexity is O(n) because it creates a new string to store the result.