def replace_char(old_string, old_char, new_char):
    new_string = ""
    for i in range(len(old_string)):
        if old_string[i] == old_char:
            new_string += new_char
        else:
            new_string += old_string[i]
    return new_string