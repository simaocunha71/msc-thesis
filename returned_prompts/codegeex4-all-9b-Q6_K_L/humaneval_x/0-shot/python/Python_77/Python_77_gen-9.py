def iscube(a):
    if a < 0:
        a = -a
    return a**0.5 == int(a**0.5)

print(iscube(1)) # ==> True
print(iscube(2)) # ==> False
print(iscube(-1)) # ==> True
print(iscube(64)) # ==> True
print(iscube(0)) # ==> True
print(iscube(180)) # ==> False