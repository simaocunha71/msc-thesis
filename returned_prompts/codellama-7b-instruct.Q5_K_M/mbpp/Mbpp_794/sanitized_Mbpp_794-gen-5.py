import re
def text_starta_endb(my_string):
    p = re.compile(r"a.*b")
    return p.match(my_string) is not None