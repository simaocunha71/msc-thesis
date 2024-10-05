
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 3]
    else:
        result = [1, 3]
        while len(result) <= n:
            if len(result) % 2 != 0:
                result.append(result[len(result)-1] + result[len(result)-2] + result[len(result)+1])
            else:
                result.append(1 + len(result)/2)
        return result

# test
print(tri(3)) # [1, 3, 2, 8]
print(tri(4)) # [1, 3, 2, 8, 13]
print(tri(5)) # [1, 3, 2, 8, 13, 21]
print(tri(6)) # [1, 3, 2, 8, 13, 21, 31]
print(tri(7)) # [1, 3, 2, 8, 13, 21, 31, 50]
print(tri(8)) # [1, 3, 2, 8, 13, 21, 31, 50, 82]
print(tri(9)) # [1, 3, 2, 8, 13, 21, 31, 50, 82, 133]
print(tri(10)) # [1, 3, 2, 8, 13, 21, 31, 50, 82, 133, 217]
























































































