```
def extract_quotation(s):
    result = []
    temp = ''
    in_quote = False
    for char in s:
        if char == '"':
            in_quote = not in_quote
        elif in_quote:
            temp += char
        else:
            if temp:
                result.append(temp)
                temp = ''
    return result
```


The function `extract_quotation` iterates over the input string `s`. It keeps track of whether it's currently inside a quotation mark or not using the `in_quote` variable. If `in_quote` is `True`, it appends characters to the `temp` string until it encounters another quotation mark, at which point it adds the `temp` string to the `result` list and resets `temp`. If `in_quote` is `False`, it adds the `temp` string to the `result` list if it's not empty, and resets `temp`. The function returns the `result` list. 

The unit test `assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']` ensures that the function correctly extracts the values between quotation marks. 





```
import re
def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```
This function uses the `re.findall` function to find all occurrences of the pattern '"([^"]*)"' in the input string `s`. The pattern '"([^"]*)"' matches a quotation mark followed by any characters (captured in a group) that are not quotation marks, followed by another quotation mark. The `re.findall` function returns a list of all non-overlapping matches of this pattern in the string as a list of strings. The function returns this list.

The unit test `assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']` ensures that the function correctly extracts the values between quotation marks.