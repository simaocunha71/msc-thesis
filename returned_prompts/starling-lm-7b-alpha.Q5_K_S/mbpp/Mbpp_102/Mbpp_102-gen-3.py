
def snake_to_camel(snake_string: str) -> str:
    camel_string = snake_string[0].upper()
    for i in range(1, len(snake_string)):
        if snake_string[i] == '_':
            camel_string += snake_string[i+1].upper()
        else:
            camel_string += snake_string[i]
    return camel_string


