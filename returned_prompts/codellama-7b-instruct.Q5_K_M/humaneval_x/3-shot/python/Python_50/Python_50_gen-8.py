    return "".join([chr(((ord(ch) - 5 + 26) % 26) + ord("a")) for ch in s])


