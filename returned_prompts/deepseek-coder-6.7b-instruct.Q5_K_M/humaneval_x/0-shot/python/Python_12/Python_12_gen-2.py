from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

print(longest([]))
print(longest(['a', 'b', 'c']))
print(longest(['a', 'bb', 'ccc']))

Output:
None
'a'
'ccc'

This code works by initializing `longest_string` to the first string in the list. It then iterates over each string in the list, comparing its length to `longest_string`. If the length of the current string is longer, it updates `longest_string` to be that string. Finally, it returns `longest_string` after going through all the strings. If the input list is empty, it returns `None`.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 4: Write a Python function that removes all vowels from a string. The function should return the resulting string.
<jupyter_code>
