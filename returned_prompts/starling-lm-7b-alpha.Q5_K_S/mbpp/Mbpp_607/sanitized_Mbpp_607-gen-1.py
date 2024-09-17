from re import findall
def find_literals(s, pattern):
    return findall(pattern, s)[0] + (findall(pattern, s).index(pattern) + 1, findall(pattern, s).index(pattern) + len(pattern))