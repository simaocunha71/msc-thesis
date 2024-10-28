
def snake_to_camel(snake_str):
    camel_str = ""
    for char in snake_str:
        if char == "_":
            camel_str += snake_str[snake_str.index(char)+1].upper()
        else:
            camel_str += char
    return camel_str


