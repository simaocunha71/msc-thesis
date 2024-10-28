
def remove_odd(string):
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])


