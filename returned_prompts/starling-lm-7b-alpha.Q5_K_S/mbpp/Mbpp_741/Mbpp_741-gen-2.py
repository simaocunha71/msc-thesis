"""
def all_Characters_Same(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if len(s) > 2:
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                return False
        return True
"""

def all_Characters_Same(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if len(s) > 2:
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                return False
        return True

print(all_Characters_Same("python")) # False
print(all_Characters_Same("pp")) # True
print(all_Characters_Same("ppp")) # True
print(all_Characters_Same("ppay")) # True
print(all_Characters_Same("abc")) # False
print(all_Characters_Same("abcabc")) # True
print(all_Characters_Same("123")) # True
print(all_Characters_Same("")) # True

# Output:
# False
# True
# True
# True
# False
# True
# True
# True
# True
# True
"""

def all_Characters_Same(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if len(s) > 2:
        for i in range(len(s)-1):
            if s[i]