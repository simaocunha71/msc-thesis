```
def extract_values(s):
    result = []
    start = None
    for i, c in enumerate(s):
        if c == '"':
            if start is None:
                start = i
            elif i > start + 1:
                result.append(s[start+1:i])
                start = None
    return result
```    
The function `extract_values` iterates over the input string `s` and checks for the character `"`. When it finds a `"`, it records the starting position of the potential value. Then, it continues to the next `"`. If the value is not empty, it appends the value to the result list. If the value is empty (i.e., the second `"` is the same as the first), it discards the value. Finally, it returns the list of extracted values. 

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function correctly extracts the values from the input string. 

The function can be used to extract values from a string that is formatted as a list of values between quotation marks. For example, you can use it to extract programming languages from a string. 

Note: The function assumes that the input string is well-formatted, i.e., it has an even number of quotation marks and each value is enclosed in double quotation marks. If the input string is not well-formatted, the function may not work correctly. 