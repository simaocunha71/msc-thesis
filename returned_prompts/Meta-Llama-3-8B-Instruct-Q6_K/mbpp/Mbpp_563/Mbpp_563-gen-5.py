```
def extract_values(s):
    result = []
    start = end = 0
    while True:
        start = s.find('"', start)
        if start == -1:
            break
        end = s.find('"', start + 1)
        result.append(s[start + 1:end])
        start = end + 1
    return result
```
The function `extract_values` takes a string `s` as input and returns a list of strings that are enclosed in quotation marks. It iterates over the string, finds the start and end indices of the quotation marks, and appends the substring between them to the result list. The function uses the `find` method to locate the quotation marks and the `append` method to add the extracted values to the list. The function returns the list of extracted values. The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function correctly extracts the values between quotation marks from the input string. 

The function starts searching for the quotation marks from the beginning of the string. If it finds a quotation mark, it continues searching from the next character until it finds the matching quotation mark. The substring between the quotation marks is then added to the result list. The function continues this process until it has processed the entire string. The `break` statement is used to exit the loop when the function has processed the entire string. 

This function assumes that the quotation marks are not nested, i.e., there are no quotation marks within the quotation marks. If the input string contains nested quotation marks, the function may not work correctly. 

The time complexity of this function is O(n), where n is the length of the input string, because it iterates over the string once. The space complexity is O(m), where m is the number of values enclosed in quotation marks, because it stores the extracted values in a list. 

The function can be modified to handle nested quotation marks by implementing a recursive function that parses the string and extracts the values between the quotation marks. However, this would increase the complexity of the function and make it less efficient. 

In summary, the function `extract_values` is a simple and efficient solution for extracting values between quotation marks from a string. It is suitable for most use cases, but it may not work correctly if the input string contains nested quotation marks. 