
def encrypt(s):
    return "".join(chr((ord(c) - ord('a') + 2 * 2) % 26 + ord('a')) for c in s)
