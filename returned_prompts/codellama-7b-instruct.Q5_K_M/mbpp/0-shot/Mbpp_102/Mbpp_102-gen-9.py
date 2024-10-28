def snake_to_camel(snake_case):
    parts = snake_case.split('_')
    return parts[0] + ''.join(map(str.title, parts[1:]))
