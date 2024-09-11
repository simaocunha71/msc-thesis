def reverse_vowels(s):
    vowel = "aeiou"
    s = list(s)
    i,j = 0,len(s)-1
    while i < j:
        if s[i] in vowel:
            s[i],s[j] = s[j],s[i]
            j -= 1
        else:
            i += 1
    return "".join(s)

reverse_vowels("Python") # "Python"

"""
Time complexity: O(n)
Space complexity: O(1)
"""


# Python3 program to print the
# reverse of the vowels

"""
def reverseVowels(s):
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and s[i] not in "aeiouAEIOU":
            i += 1
        while i < j and s[j] not in "aeiouAEIOU":
            j -= 1

        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)
"""


# This code contributed by
# Saurabh Thapliyal

```
reverse_vowels("Python") # "Python"
```

```
def reverse_vowels(s):
    s = list(s)
    i,j = 0,len(s)-1
    vowel = "aeiou"
    while i < j:
        if s[i] in vowel:
            s[i],s[j] = s[j],s[i]
            j -= 1
        else:
            i += 1
    return "".join(s)
```
reverse_vowels("Python") # "Python"

```python
"""
Time complexity: O(n)
Space complexity: O(1)
"""
```

```python
"""
Write a python function to reverse only