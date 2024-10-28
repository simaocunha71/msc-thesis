
def replace_spaces(str):
    new_str = ""
    for i in str:
        if i == " ":
            new_str += "%20"
        else:
            new_str += i
    return new_str


