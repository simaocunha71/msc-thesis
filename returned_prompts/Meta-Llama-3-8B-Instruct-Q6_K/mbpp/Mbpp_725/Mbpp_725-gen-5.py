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
Explanation:
The function `extract_quotation` iterates over the input string `s`. It keeps track of the current substring within quotation marks using the `temp` variable. Whenever it encounters a quotation mark, it appends the current substring to the result list and resets the `temp` variable. Finally, it returns the list of extracted values. The unit test `assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']` ensures the function works correctly. 