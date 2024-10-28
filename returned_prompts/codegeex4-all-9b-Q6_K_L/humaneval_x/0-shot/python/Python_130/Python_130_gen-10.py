def tri(n):
    if n==0: return [3]
    if n==1: return [1, 3]
    if n==2: return [1, 3, 2]
    a = [1, 3, 2]
    for i in range(3, n+1):
        if i%2==0:
            a.append(1 + i / 2)
        else:
            a.append(a[i-1] + a[i-2] + a[i+1])
    return a

print(tri(1))
print(tri(2))
print(tri(3))
print(tri(4))
print(tri(5))
print(tri(6))
print(tri(7))
print(tri(8))
print(tri(9))
print(tri(10))
print(tri(11))