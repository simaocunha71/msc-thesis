
def anti_shuffle(s):
    words = s.split()
    return ' '.join([sorted(word) for word in words])


def anti_shuffle(s):
    return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x))))


def anti_shuffle(s):
    return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x, reverse=True))))


def anti_shuffle(s):
    return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x, reverse=True)), reverse=True))
