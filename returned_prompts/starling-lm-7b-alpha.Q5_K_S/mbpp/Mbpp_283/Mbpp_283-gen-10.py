"""
def validate(n):
    if(n < 0):
        return False
    n = str(n)
    d = {}
    for i in n:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d:
        if d[i] > int(i):
            return False
    return True
"""

def validate(n):
    if(n < 0):
        return False
    n = str(n)
    d = {}
    for i in n:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d:
        if d[i] > int(i):
            return False
    return True

#print(validate(1234))
print(validate(9876))
print(validate(123))
print(validate(1123))
print(validate(124))
print(validate(12345))
print(validate(123456))
print(validate(1234567))
print(validate(12345678))
print(validate(123456789))
print(validate(1234567890))
print(validate(12345678901))
print(validate(123456789012))
print(validate(1234567890123))
print(validate(12345678901234))
print(validate(123456789012345))
print(validate(1234567890123456))
print(validate(12345678901234567))
print(validate(123456789012345678))
print(validate(1234567890123456789))
print(validate