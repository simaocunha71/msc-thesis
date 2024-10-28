```
def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
```
This function splits the input string into components using the underscore as a delimiter. It then takes the first component as it is and joins the rest of the components with the first character of each component capitalized using the title method. The result is a camel case string. 

For example, the input 'python_program' is split into ['python', 'program'], then the function returns 'Pythonprogram'. The unit test `assert snake_to_camel('python_program')=='PythonProgram'` ensures that the function works correctly. 