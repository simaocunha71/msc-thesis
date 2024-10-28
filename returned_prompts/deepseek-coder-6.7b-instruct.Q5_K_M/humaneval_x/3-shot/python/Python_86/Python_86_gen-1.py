    return ' '.join(sorted(s.split(' '), key=lambda word: [ord(c) for c in word]))


