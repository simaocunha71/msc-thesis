import re
def move_num(string):
    return ''.join(re.split(r'(\d+)', string))