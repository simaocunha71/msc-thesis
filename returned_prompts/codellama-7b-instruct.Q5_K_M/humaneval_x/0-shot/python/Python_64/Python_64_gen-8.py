
def vowels_count(s):
    vowels = set('aeiou')
    if s[-1] == 'y':
        vowels.add('y')
    return sum(1 for c in s if c.lower() in vowels)

B:

def vowels_count(s):
    vowels = set('aeiou')
    y = False
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
        elif c.lower() == 'y':
            y = True
    return count if y else count - 1

C:

def vowels_count(s):
    count = 0
    for c in s:
        if c.lower() in set('aeiouy'):
            count += 1
    return count

D:

def vowels_count(s):
    vowels = set('aeiou')
    if s[-1] == 'y':
        vowels.add('y')
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
    return count

E:

def vowels_count(s):
    count = 0
    for c in s:
        if c.lower() in set('aeiou'):
            count += 1
    return count

F:

def vowels_count(s):
    count = 0
    for c in s:
        if c.lower() in set('aeiouy'):
            count += 1
        elif c.lower() == 'y':
            count -= 1
    return count

G:

def vowels_count(s):
    vowels = set('aeiou')
    if s[-1] == 'y':
        vowels.add('y')
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
    return count

H:

def vowels_count(s):
    v