"""
def validate(n):
    digits = [int(i) for i in str(n)]
    for digit in digits:
        if digits.count(digit) > digit:
            return False
    return True

print(validate(1234))
"""

def validate(n):
    digits = [int(i) for i in str(n)]
    for digit in digits:
        if digits.count(digit) > digit:
            return False
    return True

print(validate(1234))

# def validate(n):
#     digits = [int(i) for i in str(n)]
#     for digit in digits:
#         if digits.count(digit) > digit:
#             return False
#     return True

# print(validate(1234))


# def validate(n):
#     n = str(n)
#     for digit in n:
#         if n.count(digit) > int(digit):
#             return False
#     return True

# print(validate(1234))

# def validate(n):
#     if len(str(n)) == len(set(str(n))):
#         return True
#     else:
#         return False

# print(validate(1234))

# def validate(n):
#     n = str(n)
#     for i in n:
#         if n.count(i) > int(i):
#             return False
#     return True

# print(validate(1234))


# def validate(n):
#     if len(set(str(n))) == len(str(n)):
#         return True
#     else:
#         return False

# print(validate(1234))


# def validate(n):
#     if len(set(str(n))) == len(str(n)):
#         return True
#     else:
#         return False

# print(validate(1234))


# def validate(n):
#     n = str(