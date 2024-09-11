"""
def sum_length(names):
    total = 0
    for name in names:
        if name[0] != 'd':
            total += len(name)
    return total

def sample_nam(names):
    total = 0
    for name in names:
        if name[0] != 'd':
            total += len(name)
    return total

print(sum_length(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
"""

def sum_length(names):
    total = 0
    for name in names:
        if name[0].lower() != 'd':
            total += len(name)
    return total

# print(sum_length(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))

def sample_nam(names):
    total = 0
    for name in names:
        if name[0].lower() != 'd':
            total += len(name)
    return total

# print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))


def test_sum_length():
    assert sum_length(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    print("All tests passed")

def test_sample_nam():
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    print("All tests passed")

test_sum_length()
test_sample_nam()

```