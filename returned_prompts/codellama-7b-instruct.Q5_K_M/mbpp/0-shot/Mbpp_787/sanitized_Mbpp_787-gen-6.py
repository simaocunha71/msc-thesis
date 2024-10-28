import re
def text_match_three(my_string):
    p = re.compile(r'a(b){3}')
    return p.search(my_string)