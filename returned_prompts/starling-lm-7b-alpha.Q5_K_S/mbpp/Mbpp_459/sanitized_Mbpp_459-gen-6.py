def is_lowercase(char):
    return char.islower()
def remove_uppercase(s):
    return ''.join(filter(is_lowercase, s))