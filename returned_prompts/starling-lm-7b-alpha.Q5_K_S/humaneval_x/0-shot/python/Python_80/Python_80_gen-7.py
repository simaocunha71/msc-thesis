    def is_happy(s):
        if len(s) < 3:
            return False

        seen = set()
        for i in range(len(s)-2):
            t = s[i:i+3]
            if t in seen:
                return False
            seen.add(t)

        return True

# Test cases
print(is_happy('a'))      # False
print(is_happy('aa'))     # False
print(is_happy('abcd'))   # True
print(is_happy('aabb'))   # False
print(is_happy('adb'))    # True
print(is_happy('xyy'))    # False
print(is_happy('xyz'))    # True






def is_happy(s):
    if len(s) < 3:
        return False

    seen = set()
    for i in range(len(s)-2):
        t = s[i:i+3]
        if t in seen:
            return False
        seen.add(t)

    return True

# Test cases
print(is_happy('a'))      # False
print(is_happy('aa'))     # False
print(is_happy('abcd'))   # True
print(is_happy('aabb'))   # False
print(is_happy('adb'))    # True
print(is_happy('xyy'))    # False
print(is_happy('xyz'))    # True






def is_happy(s):
    if len(s) < 3:
        return False

    seen = set()
    for i in range(len(s)-2):
        t = s[i:i+3]
        if t in seen:
            return False
        seen.add(t)

    return True

# Test cases
print(is_happy('a'))      # False
print(is_happy('aa'))     # False
print(is_happy('abcd'))   # True
print(is_happy('aabb'))  