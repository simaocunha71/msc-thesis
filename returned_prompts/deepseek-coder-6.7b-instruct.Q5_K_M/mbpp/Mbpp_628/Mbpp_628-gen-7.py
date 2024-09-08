def replace_spaces(s: str) -> str:
    return s.replace(' ', '%20')

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return s.replace(' ', '%20')

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return '%20'.join(s.split(' '))

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return ''.join(['%20' + i if i == ' ' else i for i in s])

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return ''.join(['%20' * (i == ' ') + j for i, j in zip(' ' + s, s + ' ')])

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return ''.join(['%20' if c == ' ' else c for c in s])

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -> str:
    return '%20'.join(s.split())

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

"""

def replace_spaces(s: str) -