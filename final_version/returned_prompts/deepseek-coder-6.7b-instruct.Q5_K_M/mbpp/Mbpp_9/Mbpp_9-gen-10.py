def find_Rotations(s: str):
    n = len(s)
    temp = s + s
    for i in range(1, n):
        if temp[i:i+n] == s:
            return i
    return n

assert find_Rotations("aaaa") == 1
assert find_Rotations("abcde") == 5
assert find_Rotations("a") == 1
assert find_Rotations("ab") == 2
assert find_Rotations("aaaab") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("cdab") == 2
assert find_Rotations("dcba") == 4
assert find_Rotations("aaaac") == 1
assert find_Rotations("baaaa") == 1
assert find_Rotations("aaaaa") == 1
assert find_Rotations("cd") == 2
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("cdab") == 2
assert find_Rotations("baaa") == 1
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("cdab") == 2
assert find_Rotations("baaa") == 1
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_Rotations("cdab") == 2
assert find_Rotations("baaa") == 1
assert find_Rotations("aaaa") == 1
assert find_Rotations("abcd") == 4
assert find_Rotations("dcba") == 4
assert find_