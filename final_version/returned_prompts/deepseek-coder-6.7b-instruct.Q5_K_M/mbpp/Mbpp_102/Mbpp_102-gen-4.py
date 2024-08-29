def snake_to_camel(s):
    s = s.split('_')
    return ''.join(i.title() for i in s)

print(snake_to_camel('python_program'))

"""
Output:
PythonProgram
"""

