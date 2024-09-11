"""
def validate(n):
    dig = str(n)
    for i in dig:
        if dig.count(i) > int(i):
            return False
    return True
"""

# or

def validate(n):
    dig = str(n)
    for i in dig:
        if dig.count(i) > int(i):
            return False
    return True

# test case
print(validate(1234)) # True
print(validate(123)) # True
print(validate(1233)) # False
print(validate(12)) # True
print(validate(1)) # True







```
