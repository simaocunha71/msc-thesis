
    if len(s) < 3:
        return False
    else:
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) != 3:
                return False
        return True

print(is_happy('a')) # False
print(is_happy('aa')) # False
print(is_happy('abcd')) # True
print(is_happy('aabb')) # False
print(is_happy('adb')) # True
print(is_happy('xyy')) # False
print(is_happy('')) # False
print(is_happy('abcabcabc')) # True
print(is_happy('abcabcabcabc')) # True
print(is_happy('abcabcabcabcabc')) # True
print(is_happy('abcdabcdabcd')) # False
print(is_happy('abcabcabcabcabcabcabc')) # True
print(is_happy('abcabcabcabcabcabcabcabcabcabc')) # True
print(is_happy('aabbaabbaabbaabb')) # False
print(is_happy('abcdefgabcdefgabcdefg')) # False
print(is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc