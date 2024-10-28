import re
def move_num(s):
    return "".join(filter(lambda x: not x.isdigit(), s)) + "".join(filter(lambda x: x.isdigit(), s))