def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
    '''
    camel_str = ''
    for i in range(len(snake_str)):
        if i == 0:
            camel_str += snake_str[i].upper()
        else:
            if snake_str[i] == '_':
                camel_str += snake_str[i+1].upper()
            else:
                camel_str += snake_str[i]
    return camel_str

# Test
print(snake_to_camel('python_program')) # PythonProgram

def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
    '''
    return ''.join(i.capitalize() or i for i in snake_str.split('_'))

# Test
print(snake_to_camel('python_program')) # PythonProgram

def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
    '''
    return ''.join(i.capitalize() or i for i in snake_str.split('_'))

# Test
print(snake_to_camel('python_program')) # PythonProgram

def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
    '''
    return ''.join(i.capitalize() or i for i in snake_str.split('_'))

# Test
print(snake_to_camel('python_program')) # PythonProgram

def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
    '''
    return ''.join(i.capitalize() or i for i in snake_str.split('_'))

# Test
print(snake_to_camel('python_program')) # PythonProgram

def snake_to_camel(snake_str):
    '''
    Convert a snake case string to camel case string
