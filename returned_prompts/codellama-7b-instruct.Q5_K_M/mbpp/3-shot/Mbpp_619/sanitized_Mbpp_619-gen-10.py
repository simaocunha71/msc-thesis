import re
def move_num(input_string):
    pattern = re.compile(r'\d+')
    return pattern.sub('', input_string) + pattern.findall(input_string)