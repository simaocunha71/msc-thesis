```
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)
```  # O(n) time complexity where n is the length of the string
```
Explanation:
This function takes a snake case string as an input and converts it to camel case string. It does this by splitting the input string into components using the underscore character as a delimiter. Then it joins these components back together using a loop, but with the first character of each component in lowercase and the rest of the characters in uppercase. The result is a camel case string. 

The time complexity of this function is O(n) where n is the length of the input string, because it needs to iterate over each character in the string. The space complexity is also O(n) because it needs to store the components of the input string in memory. 

The unit test `assert snake_to_camel('python_program')=='PythonProgram'` ensures that the function works correctly. It checks that the function converts the snake case string 'python_program' to the camel case string 'PythonProgram'. 

This function assumes that the input string is a valid snake case string, i.e., it only contains lowercase letters, digits, and underscores. If the input string is not a valid snake case string, the function may not work correctly. 
```python
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

assert snake_to_camel('python_program')=='PythonProgram'
```  # O(n) time complexity where n is the length of the string
```
Explanation:
This function takes a snake case string as an input and converts it to camel case string. It does this by splitting the input string into components using the underscore character as a delimiter. Then it joins these components back together using a loop, but with the first character of each component in lowercase and the rest of the characters in uppercase. The result is a camel case string. 

The time complexity of this function is O(n) where n is the length of the input string, because it needs to iterate over each character in the string. The space complexity is also O(n) because it needs to store the components of the input string in memory. 

The unit test `assert snake_to_camel('python_program')=='PythonProgram'` ensures that the function works correctly. It checks that the function converts the snake case string 'python