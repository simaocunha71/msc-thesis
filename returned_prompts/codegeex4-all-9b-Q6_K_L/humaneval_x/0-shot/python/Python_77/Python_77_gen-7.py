def iscube(a):
    if a==0:
        return True
    if a<0:
        a=-a
    i=1
    while i**3<=a:
        if i**3==a:
            return True
        i+=1
    return False

print(iscube(1)) #True
print(iscube(2)) #False
print(iscube(-1)) #True
print(iscube(64)) #True
print(iscube(0)) #True
print(iscube(180)) #False