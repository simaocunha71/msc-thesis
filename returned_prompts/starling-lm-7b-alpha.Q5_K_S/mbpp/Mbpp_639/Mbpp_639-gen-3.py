"""
def sample_nam(names):
    length = 0
    for name in names:
        if name[0].isupper():
            length += len(name)
    return length
"""

def sample_nam(names):
    length = 0
    for name in names:
        if name[0].isupper():
            length += len(name)
    return length


# print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
# print(sample_nam(['sally', 'dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))





"""
def test_sample_nam():
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(['sally', 'dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==11
test_sample_nam()
"""





def sample_nam(names):
    length = 0
    for name in names:
        if name[0].isupper():
            length += len(name)
    return length

def test_sample_nam():
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(['sally', 'dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==11
test_sample_nam()





def sample_nam(names):
    length = 0
    for name in names:
        if name[0].isupper():
            length += len(name)
    return length

# print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
# print(sample_nam(['sally', 'dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))


def test_sample_nam():
    assert sample_nam(['sally', 'Dylan', 'rebecca