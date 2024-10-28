```
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)
```


This function works by splitting the snake case string into components using the underscore as a delimiter. It then joins these components back together, but with the first character of each component capitalized using the title() method. This results in a camel case string. For example, the input 'python_program' would be converted to 'PythonProgram'. The unit test provided, `assert snake_to_camel('python_program')=='PythonProgram'`, ensures that this function works correctly. 