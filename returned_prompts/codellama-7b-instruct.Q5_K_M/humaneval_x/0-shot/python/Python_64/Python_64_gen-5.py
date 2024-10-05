
def vowels_count(s):
    count = 0
    vowels = 'aeiouy'
    for c in s:
        if c in vowels:
            count += 1
    return count

B:

def vowels_count(s):
    return len([c for c in s if c in 'aeiouy'])

C:

def vowels_count(s):
    count = 0
    for c in s:
        if c in 'aeiouy':
            count += 1
    return count

D:

def vowels_count(s):
    return sum(c in 'aeiouy' for c in s)

E:

def vowels_count(s):
    return sum(map(s.count, 'aeiouy'))

F:

def vowels_count(s):
    return sum(s.count(c) for c in 'aeiouy')

G:

def vowels_count(s):
    count = 0
    for c in s:
        if c in 'aeiouy':
            count += 1
    return count

H:

def vowels_count(s):
    return len('aeiouy'.find(c) for c in s)

I:

def vowels_count(s):
    return len(set('aeiouy').intersection(s))
