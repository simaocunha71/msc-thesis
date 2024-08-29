def sample_nam(names):
    sum = 0
    for name in names:
        if name[0].isupper():
            sum += len(name)
    return sum

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

