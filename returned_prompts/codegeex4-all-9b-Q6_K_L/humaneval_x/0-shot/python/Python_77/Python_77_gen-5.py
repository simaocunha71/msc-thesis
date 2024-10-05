def iscube(a):
    if a >= 0:
        return round(a ** (1. / 3)) ** 3 == a
    else:
        return False

print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False