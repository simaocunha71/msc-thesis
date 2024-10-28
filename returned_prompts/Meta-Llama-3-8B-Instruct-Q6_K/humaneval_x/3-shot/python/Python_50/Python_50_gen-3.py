    return "".join([chr(((ord(ch) - ord("a")) % 26) + ord("a")) for ch in s])  # decode by shifting back by 5


