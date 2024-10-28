
def is_happy(s):
    if len(s) < 3:
        return False

    return len(set(s[i:i+3] for i in range(0, len(s), 3))) == len(s) // 3


# Testing
print(is_happy("a"))  # False
print(is_happy("aa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False





def is_happy(s):
    if len(s) < 3:
        return False

    seen = set()
    for i in range(0, len(s), 3):
        if s[i:i+3] in seen:
            return False
        seen.add(s[i:i+3])

    return True


# Testing
print(is_happy("a"))  # False
print(is_happy("aa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False





def is_happy(s):
    if len(s) < 3:
        return False

    seen = set()
    for i in range(0, len(s), 3):
        if s[i:i+3] in seen:
            return False
        else:
            seen.add(s[i:i+3])
    return True


# Testing
print(is_happy("a"))  # False
print(is_happy("aa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False




