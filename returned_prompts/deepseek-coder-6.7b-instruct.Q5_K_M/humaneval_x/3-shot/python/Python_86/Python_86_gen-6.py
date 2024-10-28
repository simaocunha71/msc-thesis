    return " ".join(sorted([w for w in s.split(" ")], key=lambda x: [ord(c) for c in x]))


