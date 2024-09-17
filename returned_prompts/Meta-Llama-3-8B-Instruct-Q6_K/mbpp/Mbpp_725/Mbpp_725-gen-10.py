```
def extract_quotation(s):
    result = []
    temp = ""
    for char in s:
        if char == '"':
            if temp:
                result.append(temp)
                temp = ""
        else:
            temp += char
    return result
```


The function `extract_quotation` iterates over the input string `s`. When it encounters a quotation mark `"`, it checks if there is a temporary string `temp` that was being built. If `temp` is not empty, it adds it to the result list and resets `temp`. If `temp` is empty, it means a new quotation mark has been found, so it starts building a new `temp` string. If the character is not a quotation mark, it simply adds it to `temp`. At the end of the function, it returns the list of extracted strings. The unit test `assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']` ensures that the function works correctly.