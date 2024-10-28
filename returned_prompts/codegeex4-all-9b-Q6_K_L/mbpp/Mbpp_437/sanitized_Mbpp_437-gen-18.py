def remove_odd(s):
    return ''.join([char for char in s if (s.index(char)+1)%2==0])