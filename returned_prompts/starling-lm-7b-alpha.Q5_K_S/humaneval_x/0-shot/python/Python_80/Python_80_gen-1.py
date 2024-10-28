
def is_happy(s):
    if len(s) < 3:
        return False
    else:
        return len(set(s[i:i+3] for i in range(len(s)-2))) == len(s[:-2])

# Alternative solution using list comprehension
def is_happy(s):
    return len({s[i:i+3] for i in range(len(s)-2)}) == len(s[:-2])

# Test cases
print(is_happy("aa"))  # False
print(is_happy("aaa"))  # False
print(is_happy("abcd"))  # True
print(is_happy("aabb"))  # False
print(is_happy("adb"))  # True
print(is_happy("xyy"))  # False
print(is_happy("abcabc"))  # True
print(is_happy("abcabcabc"))  # False

# Bonus: Check if all the characters in the string are the same
def is_happy_all_same(s):
    return len(s) <= 2 or len(set(s)) == 1

# Test cases
print(is_happy_all_same("aa"))  # True
print(is_happy_all_same("aaa"))  # True
print(is_happy_all_same("abcd"))  # False
print(is_happy_all_same("aabb"))  # False
print(is_happy_all_same("adb"))  # False
print(is_happy_all_same("xyy"))  # False
print(is_happy_all_same("abcabc"))  # False
print(is_happy_all_same("abcabcabc"))  # False

```
