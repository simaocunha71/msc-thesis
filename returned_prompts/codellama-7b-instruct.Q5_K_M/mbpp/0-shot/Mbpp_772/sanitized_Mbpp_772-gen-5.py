import re
def remove_length(string, k):
    pattern = r'\w{{{}}}'.format(k)
    return re.sub(pattern, '', string)