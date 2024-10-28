```
def snake_to_camel(s):
    components = s.split('_')
    return ''.join(x.title() for x in components)
```
The problem is asking to write a function that takes a string in snake case (e.g., 'python_program') and converts it to a string in camel case (e.g., 'PythonProgram'). 

The unit test provided, `assert snake_to_camel('python_program')=='PythonProgram'`, gives us an idea of the expected output.

Here's how we can solve this problem:
- Split the input string into components using the underscore character as the separator.
- Use a list comprehension to capitalize each component (except the first one) and join them together with no separator.

The `title()` method is used to capitalize each component, and the `join()` method is used to concatenate the components into a single string. The `''` before `join()` is used to specify that there should be no separator between the components.

This solution works by splitting the input string into components, capitalizing each component (except the first one), and then joining them together into a single string. The result is a string in camel case. 

For example, if we call `snake_to_camel('python_program')`, it will return `'PythonProgram'`, which is the expected output. 