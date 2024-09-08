def string_sequence(n):
    return ' '.join(map(str, range(n+1)))

B:
def string_sequence(n):
    string = ""
    for i in range(n+1):
        string += str(i)
        if i != n:
            string += " "
    return string

C:
def string_sequence(n):
    string = ""
    for i in range(n+1):
        string += str(i) + " "
    return string.strip()

D:
def string_sequence(n):
    return ' '.join(str(i) for i in range(n+1))

E:
def string_sequence(n):
    return "0 1 2 3 4 5"

F:
def string_sequence(n):
    return ''.join(str(i) for i in range(n+1))

G:
def string_sequence(n):
    return ' '.join(map(str, range(0, n+1)))

H:
def string_sequence(n):
    return ' '.join(str(i) for i in range(n+1))

I:
def string_sequence(n):
    return ''.join(str(i) for i in range(n+1))

J:
def string_sequence(n):
    return ' '.join(str(i) for i in range(n+1), ' ')

