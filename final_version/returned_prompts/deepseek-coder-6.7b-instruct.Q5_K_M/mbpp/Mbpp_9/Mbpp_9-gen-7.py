def find_Rotations(s: str):
    n = len(s)
    temp = s + s
    for i in range(1, n):
        if temp[i:i+n] == s:
            return i
    return n

print(find_Rotations("aaaa"))  # Output: 1


