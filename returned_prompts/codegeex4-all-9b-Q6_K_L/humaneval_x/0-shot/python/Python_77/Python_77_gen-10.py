def iscube(a):
    if a==0:
        return True
    for i in range(-abs(a),abs(a)):
        if i**3==a:
            return True
    return False

print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))