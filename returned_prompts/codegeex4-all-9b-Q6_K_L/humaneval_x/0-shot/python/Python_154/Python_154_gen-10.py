def cycpattern_check(a , b):
    def rotate_string(s):
        return s[1:] + s[0]

    rotations = [rotate_string(b) for _ in range(len(b))]
    return any(rotation in a for rotation in rotations)

print(cycpattern_check("abcd","abd")) # False
print(cycpattern_check("hello","ell")) # True
print(cycpattern_check("whassup","psus")) # False
print(cycpattern_check("abab","baa")) # True
print(cycpattern_check("efef","eeff")) # False
print(cycpattern_check("himenss","simen")) # True