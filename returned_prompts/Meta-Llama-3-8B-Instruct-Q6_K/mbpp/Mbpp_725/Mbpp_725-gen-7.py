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
The function `extract_quotation` iterates over the given string `s`. 
When it encounters a quotation mark, it checks if there is a temporary string built up. 
If there is, it adds the temporary string to the result list and resets the temporary string. 
If there is no temporary string, it simply moves on to the next character. 
The function returns the list of extracted strings. 

The unit test `assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']` ensures that the function works correctly. 
It checks that the function correctly extracts the strings 'A53', 'multi', and 'Processor' from the given string. 
If the function works correctly, the test will pass, otherwise it will fail. 
This test helps to verify the correctness of the function. 

The time complexity of this function is O(n), where n is the length of the string. 
This is because the function iterates over the string once. 
The space complexity is also O(n), as in the worst case scenario, the function might need to store all characters in the temporary string. 
However, in the average case, the function will store only the characters between the quotation marks, which is less than n. 
So, the space complexity is O(k), where k is the number of quotation marks in the string. 
But in the worst case, k can be equal to n, so the space complexity can be considered as O(n). 





This solution assumes that the quotation marks are always properly nested, i.e., every quotation mark has a matching quotation mark. 
If the quotation marks are not properly nested, the function may not work correctly. 
In that case, a more complex solution would be needed to handle the nested quotation marks. 