def reverse_delete(s, c):
    s = s.translate({ord(i): None for i in c})
    return (s, 'True') if s == s[::-1] else (s, 'False')

B:
def reverse_delete(s, c):
    s = s.translate(str.maketrans('', '', c))
    return (s, 'True') if s == s[::-1] else (s, 'False')

C:
def reverse_delete(s, c):
    s = ''.join(x for x in s if x not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

D:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

E:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

F:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

G:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

H:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

I:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

J:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

K:
def reverse_delete(s, c):
    s = ''.join(i for i in s if i not in c)
    return (s, 'True') if s == s[::-1] else (s, 'False')

