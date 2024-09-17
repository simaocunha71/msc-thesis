def text_lowercase_underscore(input_string):
    underscore_list = input_string.split("_")
    for i in range(len(underscore_list)):
        if underscore_list[i] != underscore_list[i].lower():
            return False
    return True