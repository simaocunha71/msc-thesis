def snake_to_camel(s):
    return ''.join(word.title() for word in s.split('_'))

print(snake_to_camel('python_program'))
<jupyter_output>
PythonProgram
<jupyter_text>
Problem 2
<jupyter_code>
