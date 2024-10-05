Here is the Python solution for the problem:

```python
def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    res = []
    temp = ""
    count = 0
    for char in paren_string:
        if char == "(":
            count += 1
            temp += char
        elif char == ")":
            count -= 1
            temp += char
        if count == 0:
            res.append(temp)
            temp = ""
    return res
```

This solution works by iterating over the input string character by character. Whenever it encounters an opening parenthesis, it increments a counter and adds it to a temporary string. When it encounters a closing parenthesis, it decrements the counter and adds it to the temporary string. Whenever the counter reaches zero, it means that a complete group of parentheses has been found and it is appended to the result list.

Please note that this solution assumes that the input string is valid and contains only balanced parentheses. If the input string may contain invalid parentheses or other characters, additional error checking and handling would be needed.