def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
def sample_nam(names):
    names = [name for name in names if name[0].isupper()]
    return sum(len(name) for name in names)
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
def sample_nam(names):
    return sum(len(name) for name in filter(lambda name: name[0].isupper(), names))
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
def sample_nam(names):
    return sum(len(name) for name in (name for name in names if name[0].isupper()))
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
def sample_nam(names):
    return sum(len(name) for name in filter(lambda name: name[0].isupper(), names))
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana',