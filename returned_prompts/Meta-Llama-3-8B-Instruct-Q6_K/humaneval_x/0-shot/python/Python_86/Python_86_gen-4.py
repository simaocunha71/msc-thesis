```
def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    return ' '.join(result)
```


Explanation:
The function anti_shuffle takes a string s as input, splits it into words, and then for each word, it sorts the characters in the word in ascending order based on ASCII value. Finally, it joins the sorted words with spaces and returns the result.

Example usage:
```
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
```
Note: The function assumes that the input string contains only spaces as word separators. If the string may contain other characters as word separators (e.g., commas, tabs, etc.), the function would need to be modified to handle that.