def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    b = int(round(a ** (1. / 3.)))
    return b ** 3 == a

print(iscube(1)) # ==> True
print(iscube(2)) # ==> False
print(iscube(-1)) # ==> True
print(iscube(64)) # ==> True
print(iscube(0)) # ==> True
print(iscube(180)) # ==> False