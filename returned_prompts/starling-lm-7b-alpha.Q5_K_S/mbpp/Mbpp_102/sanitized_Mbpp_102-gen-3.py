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