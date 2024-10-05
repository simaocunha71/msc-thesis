Here is a Python solution for the problem:

```Python
import re

def selectWords(s, n):
    words = re.findall(r'\b\w+\b', s.lower())
    return [word for word in words if sum(1 for char in word if char not in 'aeiou') == n]
```

This function first converts the input string to lower case and then finds all words in the string using regular expression. Then it filters out the words that contain exactly n consonants by counting the number of consonants in each word. The result is a list of words that contain exactly n consonants. If the input string is empty, the function returns an empty list.

The regular expression `\b\w+\b` finds all sequences of word characters (letters, numbers, and underscores) that are bounded by word boundaries. The `\b` is a word boundary, which means the sequence of characters must be separated from other characters by a word boundary. The `\w+` means one or more word characters. The `+` is a quantifier that means "one or more".

The `re.findall` function returns all non-overlapping matches of the regular expression in the string, as a list of strings. The `lower` method converts the input string to lower case. The list comprehension `[word for word in words if sum(1 for char in word if char not in 'aeiou') == n]` filters out the words that contain exactly n consonants. The `sum(1 for char in word if char not in 'aeiou')` counts the number of consonants in each word. The `1 for char in word if char not in 'aeiou'` is a generator expression that yields 1 for each consonant in the word. The `sum` function adds up these 1s to get the total number of consonants. The list comprehension then returns a list of words that contain exactly n consonants. If the input string is empty, the function returns an empty list. 