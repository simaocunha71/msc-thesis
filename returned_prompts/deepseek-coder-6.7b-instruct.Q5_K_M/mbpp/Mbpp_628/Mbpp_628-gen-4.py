def replace_spaces(s):
    return s.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return "%20".join(s.split(" "))

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    result = ''
    for char in s:
        if char == ' ':
            result += '%20'
        else:
            result += char
    return result

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return s.translate(str.maketrans(" ", "%20"))

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join(['%20' if c == ' ' else c for c in s])

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join(list(map(lambda c: '%20' if c == ' ' else c, s)))

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join(filter(lambda c: '%20' if c == ' ' else c, s))

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join(["%20" if i == " " else i for i in s])

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join([i if i != ' ' else '%20' for i in s])

print(replace_spaces("My Name is Dawood"))

# Alternatively
def replace_spaces(s):
    return ''.join(["%" if i == " " else i for i in s]) + '20'

print(replace_