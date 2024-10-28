

def change_base(x, base):
    s = []
    while x > 0:
        s.append(str(x % base))
        x //= base
    return ''.join(s[::-1])
