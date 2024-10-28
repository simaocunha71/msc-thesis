
def reverse_delete(s,c):
    s = [x for x in s if x not in c]
    return ''.join(s[::-1]),s==s[::-1]

