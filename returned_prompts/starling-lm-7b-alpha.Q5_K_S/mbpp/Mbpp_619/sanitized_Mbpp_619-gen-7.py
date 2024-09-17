import re
def move_num(s):
    return s.replace(r'\d+', '') + s[::-1].replace(r'^0*', '')