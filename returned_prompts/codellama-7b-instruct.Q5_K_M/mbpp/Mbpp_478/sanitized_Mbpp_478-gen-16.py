def remove_lowercase(input_string):
    for i in range(len(input_string)):
        if input_string[i].islower():
            input_string = input_string[:i] + input_string[i+1:]
    return input_string