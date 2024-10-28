
def split_words(txt):
    if txt.count(' ') > 0:
        return txt.split(' ')
    if txt.count(',') > 0:
        return txt.split(',')
    count = 0
    for char in txt:
        if ord(char) % 2 != 0:
            count += 1
    return count

# Other Solution
def split_words(txt):
    words = txt.split()
    if len(words) == 0:
        return txt.split(',')
    return words

# Other Solution
def split_words(txt):
    if txt.count(' ') > 0:
        return txt.split(' ')
    if txt.count(',') > 0:
        return txt.split(',')
    words = []
    for char in txt:
        if ord(char) % 2 != 0:
            words.append(char)
    return len(words)

# Other Solution
def split_words(txt):
    if txt.count(' ') > 0:
        return txt.split(' ')
    if txt.count(',') > 0:
        return txt.split(',')
    count = 0
    for char in txt:
        if ord(char) % 2 != 0:
            count += 1
    return count

# Other Solution
def split_words(txt):
    if txt.count(' ') > 0:
        return txt.split(' ')
    if txt.count(',') > 0:
        return txt.split(',')
    count = 0
    for char in txt:
        if ord(char) % 2 != 0:
            count += 1
    return count

# Other Solution
def split_words(txt):
    if txt.count(' ') > 0:
        return txt.split(' ')
    if txt.count(',') > 0:
        return txt.split(',')
    count = 0
    for char in txt:
        if ord(char) % 2 != 0:
            count += 1
    return count

# Other Solution
def split