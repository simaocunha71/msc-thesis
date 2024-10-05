
def reverse_delete(s,c):
    s = s.replace(c,'')
    return (s,s == s[::-1])

