    return ' '.join(sorted([word for word in s.split()], key=lambda x: [ord(c) for c in x]))


