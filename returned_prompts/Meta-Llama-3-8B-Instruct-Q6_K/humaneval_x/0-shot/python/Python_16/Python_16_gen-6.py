Here is the solution using a Python dictionary to store the characters and their frequencies:

```
def count_distinct_characters(string: str) -> int:
    char_count = {}
    for char in string.lower():
        if char.isalnum():  # ignore spaces and punctuation
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return len(char_count)
```
In this code, we create an empty dictionary `char_count` to store the characters and their frequencies. We then iterate over each character in the input string, converting it to lowercase to ensure we are counting characters regardless of case. We use the `isalnum()` method to ignore any spaces or punctuation. If a character is already in the dictionary, we increment its count; otherwise, we add it to the dictionary with a count of 1. Finally, we return the length of the dictionary, which is the number of distinct characters in the string. This solution has a time complexity of O(n), where n is the length of the input string.