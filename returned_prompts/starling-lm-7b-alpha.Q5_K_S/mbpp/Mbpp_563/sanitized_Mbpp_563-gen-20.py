def extract_values(s):
    l = s.split('"')
    l = [i for i in l if i != '']
    return l[1::2]