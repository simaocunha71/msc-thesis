def text_lowercase_underscore(input_str):
    for i in range(len(input_str)-1):
        if (input_str[i] != "_"):
            if (input_str[i].isupper() or input_str[i].isdigit()):
                return False
    return True