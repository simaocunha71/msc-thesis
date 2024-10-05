    if txt.strip():
        return txt.split()
    else:
        return sum(1 for c in txt if c.islower() and ord(c) % 2)


