"""
Write a function to check whether an element exists within a tuple.
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
"""

def check_tuplex(tuplex):
    assert tuplex[0] == 'w',f'{tuplex}{0}'.format(tuple=tuplex)
    assert tuplex[1] == 3,f'{tuplex}{1}'.format(tuple=tuplex)
    assert tuplex[2] == 'r',f'{tuplex}{2}'.format(tuple=tuplex)
    assert tuplex[3] == 'e',f'{tuplex}{3}'.format(tuple=tuplex)
    assert tuplex[4] == 's',f'{tuplex}{4}'.format(tuple=tuplex)
    assert tuplex[5] == 'o',f'{tuplex}{5}'.format(tuple=tuplex)
    assert tuplex[6] == 'u',f'{tuplex}{6}'.format(tuple=tuplex)
    assert tuplex[7] == 'r',f'{tuplex}{7}'.format(tuple=tuplex)
    assert tuplex[8] == 'c',f'{tuplex}{8}'.format(tuple=tuplex)
    assert tuplex[9] == 'e',f'{tuplex}{9}'.format(tuple=tuplex)
    return True
