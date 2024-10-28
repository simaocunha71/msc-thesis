
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True

# test cases
print(is_happy('a'))  # False
print(is_happy('aa'))  # False
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False
print(is_happy('aab'))  # False
print(is_happy('abc'))  # True
print(is_happy('xyz'))  # True
print(is_happy('xyx'))  # False
print(is_happy('yyy'))  # False
print(is_happy('xxy'))  # False
print(is_happy('yxy'))  # False
print(is_happy('yyx'))  # False
print(is_happy('xxx'))  # True
print(is_happy('zyx'))  # True
print(is_happy('zxy'))  # True
print(is_happy('zzz'))  # False
print(is_happy('zzx'))  # False
print(is_happy('zxz'))  # False
print(is_happy('xzz'))  # True
print(is_happy('yzz'))  # True
print(is_happy('zyz'))  # True
print(is_happy(''))  # False
print(is_happy('aababab'))  # True
print(is_happy('xyzxyz'))  # True
print(is_happy('abcabcabc'))  # True
print(is_happy('123123123'))  # True
print(is_happy('1231231231'))  # False
print(is_happy('12312312312'))  # False
print(is_happy('123123123123'))  # True
print(is_