
def encrypt(s):
    rot = 2*2
    return ''.join([chr((ord(c) - ord('a') + rot) % 26 + ord('a')) for c in s])

