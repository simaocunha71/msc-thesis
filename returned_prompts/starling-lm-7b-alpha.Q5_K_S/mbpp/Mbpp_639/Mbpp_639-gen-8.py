"""
def sample_nam(names):
    l = 0
    for i in names:
        if i[0] != 'd':
            l += len(i)
    return l
"""

def sample_nam(names):
    l = 0
    for i in names:
        if i[0] != 'd' and i[0].islower():
            l += len(i)
    return l

#print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))
print(sample_nam(['Sally', 'Dylan', 'Rebecca', 'Diana', 'Joanne', 'Keith'])) # should print 16
print(sample_nam(['sally', 'Dylan', 'rebecca', 'diana', 'joanne', 'keith'])) # should print 12
print(sample_nam(['Sally', 'dylan', 'rebecca', 'Diana', 'joanne', 'keith'])) # should print 12
print(sample_nam(['Sally', 'dylan', 'REBECCA', 'DIANA', 'JOANNE', 'KEITH'])) # should print 16
print(sample_nam(['Sally', 'dylan', 'REBECCA', 'DIANA', 'JOANNE', 'KEITH', 'keith'])) # should print 22
print(sample_nam(['Sally', 'dylan', 'REBECCA', 'DIANA', 'JOANNE', 'KEITH', 'keith', 'sally'])) # should print 23
print(sample_nam(['Sally', 'dylan', 'REBECCA', 'DIANA', 'JOANNE', 'KEITH', 'keith', 'sally', 'dylan'])) # should print 28



def sample_nam(names):
    l = 0
    for i in names:
        if i[0].isupper():
            l += len(i)
    return l

#print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # should print 16
print(sample