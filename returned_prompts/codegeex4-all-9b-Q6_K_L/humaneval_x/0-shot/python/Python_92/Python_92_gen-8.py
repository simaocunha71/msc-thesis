def any_int(x, y, z):
    return sum([x,y,z]) in [x,y,z] and all(isinstance(i, int) for i in [x,y,z])

print(any_int(5, 2, 7)) #➞ True
print(any_int(3, 2, 2)) #➞ False
print(any_int(3, -2, 1)) #➞ True
print(any_int(3.6, -2.2, 2)) #➞ False