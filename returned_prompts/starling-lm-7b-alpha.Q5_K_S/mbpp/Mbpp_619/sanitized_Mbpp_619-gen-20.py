def move_num(s):
    alphanum = "".join(filter(str.isalpha, s))
    numeric = "".join(filter(str.isdigit, s))
    return alphanum + numeric