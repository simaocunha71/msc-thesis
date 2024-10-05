def iscube(a):
    if a < 0:
        a = -a
    return a**0.33 % 1 == 0

print(iscube(1)) #True
print(iscube(2)) #False
print(iscube(-1)) #True
print(iscube(64)) #True
print(iscube(0)) #True
print(iscube(180)) #False