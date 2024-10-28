def remove_odd(s):
    odd_chars = [i for i in s if ord(i) % 2 == 1]
    return ''.join([i for i in s if i not in odd_chars])