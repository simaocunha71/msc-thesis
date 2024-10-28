
def anti_shuffle(s):
    """
    >>> anti_shuffle('Hi')
    'Hi'
    >>> anti_shuffle('hello')
    'ehllo'
    >>> anti_shuffle('Hello World!!!')
    'Hello !!!Wdlor'
    """
    return ' '.join([sorted(word, key=lambda x: ord(x)) for word in s.split()])
