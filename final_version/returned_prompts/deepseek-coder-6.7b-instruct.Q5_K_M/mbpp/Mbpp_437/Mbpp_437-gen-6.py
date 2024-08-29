
def remove_odd(string):
    new_string = ""
    for i in range(0, len(string), 2):
        new_string += string[i]
    return new_string

print(remove_odd("python"))

"""
