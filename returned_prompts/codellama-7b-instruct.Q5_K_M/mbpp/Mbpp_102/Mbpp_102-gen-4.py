def snake_to_camel(snake):
    components = snake.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

# Tests
assert snake_to_camel('python_program') == 'PythonProgram'
assert snake_to_camel('python_is_great') == 'PythonIsGreat'
assert snake_to_camel('snake_case') == 'SnakeCase'


