def snake_to_camel(snake_string: str) -> str:
    camel_case_string = snake_string[0].upper() + snake_string[1:]
    return camel_case_string