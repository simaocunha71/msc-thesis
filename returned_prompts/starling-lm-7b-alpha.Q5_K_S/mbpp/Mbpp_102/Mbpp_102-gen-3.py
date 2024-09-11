def snake_to_camel(snake_str):
    camel_str = ""
    for i in range(len(snake_str)):
        if i == 0:
            camel_str += snake_str[i].upper()
        else:
            if snake_str[i] == "_":
                camel_str += snake_str[i+1].upper()
            else:
                camel_str += snake_str[i]
    return camel_str

# assert snake_to_camel('python_program')=='PythonProgram'

# Another way:
def snake_to_camel_v2(snake_str):
    return ''.join(map(lambda x: x.title(), snake_str.split('_')))

# assert snake_to_camel_v2('python_program')=='PythonProgram'

# Another way:
def snake_to_camel_v3(snake_str):
    return snake_str[0].upper() + snake_str[1:].replace('_', '')

# assert snake_to_camel_v3('python_program')=='PythonProgram'

# Another way:
def snake_to_camel_v4(snake_str):
    return ''.join(map(lambda x: x.title(), re.sub('_(.)', r'\1', snake_str).split('_')))

# assert snake_to_camel_v4('python_program')=='PythonProgram'

# Another way:
def snake_to_camel_v5(snake_str):
    return ''.join(map(lambda x: x.title(), re.sub('_(.)', r'\1', snake_str).split('_')))

# assert snake_to_camel_v5('python_program')=='PythonProgram'

# Another way:
def snake_to_camel_v6(snake_str):
    return ''.join(map(lambda x: x.title(), re.sub('_(.)', r'\1', snake_str).split('_')))

# assert snake_