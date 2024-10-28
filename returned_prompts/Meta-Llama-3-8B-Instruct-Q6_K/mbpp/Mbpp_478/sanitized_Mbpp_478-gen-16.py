def remove_lowercase(s):
    return ''.join(c for c in s if not c.islower())  # or return ''.join([c for c in s if not c.islower()]) for python 2.x