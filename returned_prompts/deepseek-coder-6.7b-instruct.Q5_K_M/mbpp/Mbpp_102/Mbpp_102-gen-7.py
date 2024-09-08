def snake_to_camel(s):
    words = s.split("_")
    return "".join(word.title() for word in words)

print(snake_to_camel('python_program'))

#Output: PythonProgram
<jupyter_output>
PythonProgram
<jupyter_text>
3. Write a Python program to remove all the occurences of a specific item from a list.
<jupyter_code>
