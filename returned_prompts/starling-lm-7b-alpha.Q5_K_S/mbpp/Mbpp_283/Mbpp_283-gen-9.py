"""
def validate(n):
    digits = str(n)
    for d in digits:
        if digits.count(d) > int(d):
            return False
    return True
"""

def validate(n):
    digits = str(n)
    for d in digits:
        if digits.count(d) > int(d):
            return False
    return True

# print(validate(1234))
# print(validate(12345))
# print(validate(123456))
# print(validate(1234567))
# print(validate(12345678))
# print(validate(123456789))
# print(validate(1234567899))



```
