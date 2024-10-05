
    return ' '.join(sorted(s.split(' '), key=lambda x: [c for c in x if c != ' ']))

print(anti_shuffle('Hi'))
print(anti_shuffle('hello'))
print(anti_shuffle('Hello World!!!'))

# Q2:

