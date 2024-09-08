def decode_shift(s):
    out = ''
    for c in s:
        w = ((ord(c) - 5 - ord('a')) % 26) + ord('a')
        out += chr(w)
    return out

# test
print(decode_shift('zwxvutspqr'))