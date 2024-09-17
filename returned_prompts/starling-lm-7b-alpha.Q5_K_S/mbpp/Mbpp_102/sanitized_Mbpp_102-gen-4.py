def snake_to_camel(snake_case):
    camel_case = ""
    for i in range(len(snake_case)):
        if(i == 0):
            camel_case += snake_case[i].upper()
        else:
            if(snake_case[i] == "_"):
                camel_case += snake_case[i+1].upper()
            else:
                camel_case += snake_case[i]
    return camel_case