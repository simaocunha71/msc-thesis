def snake_to_camel(snake):
    camel_case = ""
    for i in range(len(snake)):
        if i == 0:
            camel_case += snake[i].upper()
        elif snake[i] == "_":
            camel_case += snake[i+1].upper()
        else:
            camel_case += snake[i]
    return camel_case