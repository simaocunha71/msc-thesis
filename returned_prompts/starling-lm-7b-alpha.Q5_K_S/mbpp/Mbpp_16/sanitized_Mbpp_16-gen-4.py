def text_lowercase_underscore(input_str):
    if "_" not in input_str:
        return False
    else:
        str_list = input_str.split("_")
        for elem in str_list:
            if not(elem.isalpha() and elem.islower()):
                return False
        return True