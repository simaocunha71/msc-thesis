```
def remove_uppercase(s):
    return ''.join(c for c in s if not c.isupper())
```


This function uses a generator expression to iterate over each character in the input string. The `isupper()` method is used to check if a character is uppercase. If the character is not uppercase, it is included in the resulting string. The `join()` method is used to concatenate the characters into a single string. 

For example, if the input string is 'cAstyoUrFavoRitETVshoWs', the function will return 'cstyoravoitshos'. 

The unit test `assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'` ensures that the function works correctly. 

This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over each character in the string once. The space complexity is O(n) as well, because it creates a new string to store the result. 

This function is case-sensitive, so it will treat uppercase and lowercase letters as different characters. If you want to treat uppercase and lowercase letters as the same character, you can convert the input string to lowercase or uppercase before processing it. 

Note: The problem statement does not specify whether the function should remove all uppercase substrings or only the first occurrence of each uppercase substring. The given solution removes all uppercase characters, not substrings. If you want to remove only the first occurrence of each uppercase substring, you would need to modify the function to keep track of the last seen character and skip it if it is uppercase. 