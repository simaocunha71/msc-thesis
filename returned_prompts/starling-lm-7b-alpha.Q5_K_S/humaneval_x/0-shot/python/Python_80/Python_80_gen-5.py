    def is_happy(s):
        return len(s) >= 3 and not any(s[i:i+3] == sub for i in range(len(s) - 2) for sub in set(s[i:i+3]))

# Example usage:
print(is_happy("abc"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False





def is_happy(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        sub = s[i:i+3]
        if sub in set(s[i:i+3] for i in range(len(s) - 2)):
            return False

    return True


# Example usage:
print(is_happy("abc"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False





def is_happy(s):
    if len(s) < 3:
        return False
    unique_subs = set()
    for i in range(len(s) - 2):
        sub = s[i:i+3]
        if sub in unique_subs:
            return False
        unique_subs.add(sub)
    return True


# Example usage:
print(is_happy("abc"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False





def is_happy(s):
    if len(s) < 3:
        return False
    unique_subs = set()
    for i in range(len(s) - 2):
        sub = s[i:i+3]
        if sub in unique_subs:
            return False
