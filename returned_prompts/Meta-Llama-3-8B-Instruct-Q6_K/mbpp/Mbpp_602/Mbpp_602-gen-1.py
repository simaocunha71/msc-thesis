```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] > 1:
            return char
    return None
```


The function `first_repeated_char(s)` takes a string `s` as an argument. It first creates a dictionary `char_count` to count the occurrence of each character in the string. Then it iterates over the string again, and if it finds a character that has already been counted (i.e., its count is greater than 1), it returns that character. If no repeated character is found, it returns `None`. The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function works correctly. 

Note: This function is case-sensitive and considers whitespace as a character. If you want to ignore case and whitespace, you can preprocess the string to remove whitespace and convert it to lowercase or uppercase. For example:
```
s = s.replace(" ", "").lower()
```
Add this line before creating the `char_count` dictionary. 
```python
s = s.replace(" ", "").lower()
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char in s:
    if char_count[char] > 1:
        return char
return None
``` 
This way, the function will treat "A" and "a" as the same character, and will ignore whitespace. 
```python
assert first_repeated_char("aBc AbC") == "a"
``` 
Now the function will return "a" for the input "aBc AbC". 
```python
assert first_repeated_char("abcabc") == "a"
``` 
The function will still return "a" for the input "abcabc". 
```python
assert first_repeated_char("abcdefg") == None
``` 
The function will return None for the input "abcdefg". 
```python
assert first_repeated_char("aabbcc") == "a"
``` 
The function will return "a" for the input "aabbcc". 
```python
assert first_repeated_char("abcabcde") == "a"
``` 
The