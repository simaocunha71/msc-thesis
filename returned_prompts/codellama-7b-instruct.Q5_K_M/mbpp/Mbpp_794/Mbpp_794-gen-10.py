
import re

def text_starta_endb(my_string):
    pattern = r"a.+b"
    return re.match(pattern, my_string)


