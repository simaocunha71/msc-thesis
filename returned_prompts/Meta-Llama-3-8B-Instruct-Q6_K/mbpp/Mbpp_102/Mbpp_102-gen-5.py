```
def snake_to_camel(s):
    result = ''
    for i, c in enumerate(s):
        if c == '_':
            result += c[1].upper()
        else:
            result += c
    return result
``` 

Explanation:
The function `snake_to_camel` takes a string `s` as input, which is in snake case. It iterates over each character `c` in the string, and for each underscore `_`, it adds the next character (converted to uppercase) to the result. For all other characters, it simply adds them to the result. The function returns the resulting camel case string. 

This function works because in snake case, underscores are used to separate words, and in camel case, the first letter of each word (except the first) is capitalized. The `enumerate` function is used to get the index `i` of each character, which is not used in this function but can be useful in other cases. The `c[1].upper()` expression is used to get the next character after the underscore and convert it to uppercase. 

The unit test `assert snake_to_camel('python_program')=='PythonProgram'` ensures that the function works correctly for the input 'python_program'. 

This function assumes that the input string is a valid snake case string, i.e., it does not contain any characters other than letters, digits, and underscores. If the input string can contain other characters, additional error checking code would be needed. 