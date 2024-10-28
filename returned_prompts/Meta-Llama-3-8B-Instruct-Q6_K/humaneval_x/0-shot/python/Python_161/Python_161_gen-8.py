```
def solve(s):
    result = []
    for char in s:
        if char.isalpha():
            result.append(char.swapcase())
        else:
            result.append(char)
    if not any(char.isalpha() for char in s):
        result = result[::-1]
    return ''.join(result)
```


Explanation:
- We iterate over the input string `s` and for each character:
  - If it's a letter, we reverse its case using the `swapcase()` method and append it to the `result` list.
  - If it's not a letter, we just append it to the `result` list as it is.
- If the `result` list doesn't contain any letters (i.e., the input string is non-alphabetic), we reverse the `result` list using slicing (`[::-1]`) to achieve the desired result.
- Finally, we join the `result` list into a string using the `join()` method and return it.

This function should work correctly for the given examples and any other input strings.