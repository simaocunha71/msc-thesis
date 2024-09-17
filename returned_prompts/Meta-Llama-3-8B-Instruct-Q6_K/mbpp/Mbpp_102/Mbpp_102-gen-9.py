```
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)
```


The function `snake_to_camel` splits the input string `snake_str` into components using the underscore as a delimiter. Then, it joins these components together using the `join` method, but with each component title-cased (i.e., first letter capitalized, the rest lowercase) using the `title` method. This effectively converts the snake case string to a camel case string.

For example, when called with the string `'python_program'`, the function returns the string `'PythonProgram'`. This is because the input string is split into the components `['python', 'program']`, which are then joined together with the first letter of each component capitalized, resulting in the output string `'PythonProgram'`. 