```
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
```



Explanation:
The function `snake_to_camel` takes a snake case string as input and converts it to a camel case string. It does this by splitting the input string into components using the underscore as a separator, then capitalizing the first letter of each component (except the first one) and joining them together. The resulting string is the camel case equivalent of the input snake case string.

The unit test `assert snake_to_camel('python_program')=='PythonProgram'` ensures that the function works correctly for the given input. It checks that the output of the function is 'PythonProgram', which is the expected camel case equivalent of the input 'python_program'. If the function is implemented correctly, this test should pass.