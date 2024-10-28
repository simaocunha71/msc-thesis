    encrypted_s = ""

    for c in s:
        if c.isalpha():
            ascii_offset = 65 if c.isupper() else 97
            encrypted_s += chr((ord(c) - ascii_offset + 2*2) % 26 + ascii_offset)
        else:
            encrypted_s += c

    return encrypted_s


