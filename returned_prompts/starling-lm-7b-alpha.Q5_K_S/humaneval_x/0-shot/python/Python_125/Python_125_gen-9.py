
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for i in txt:
            if ord(i) % 2 == 1:
                count += 1
        return count

# Alternative solution
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([i for i in txt if chr(ord(i) + 1) in 'abcdefghijklmnopqrstuvwxyz'])

# Alternative solution
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return txt.count('a') + txt.count('c') + txt.count('e') + txt.count('g') + txt.count('i') + txt.count('k') + txt.count('l') + txt.count('m') + txt.count('o') + txt.count('p') + txt.count('r') + txt.count('t') + txt.count('u') + txt.count('w') + txt.count('y')


# Alternative solution
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([i for i in txt if chr(ord(i) + 1) in 'abcdefghijklmnopqrstuvwxyz'])


# Alternative solution
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([i for i in txt if chr(ord(i) + 1) in 'abcdefghijklmnopqrstuvwxyz'])

