def snake_to_camel(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

# Testing
print(snake_to_camel('python_program'))  # Output: PythonProgram

# Alternative solution using list comprehension
def snake_to_camel(s: str) -> str:
    return ''.join([word.capitalize() for word in s.split('_')])

# Testing
print(snake_to_camel('python_program'))  # Output: PythonProgram

