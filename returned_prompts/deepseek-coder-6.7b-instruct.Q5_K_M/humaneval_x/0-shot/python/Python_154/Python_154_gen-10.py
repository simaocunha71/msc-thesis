
def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1:] + b[:-1]
    return False

print(cycpattern_check("abcd","abd")) # False
print(cycpattern_check("hello","ell")) # True
print(cycpattern_check("whassup","psus")) # False
print(cycpattern_check("abab","baa")) # True
print(cycpattern_check("efef","eeff")) # False
print(cycpattern_check("himenss","simen")) # True

# The function works by rotating the second string b by one character to the left at each step and checking if this new string is a substring of the first string a.
# If a rotation of b is found in a, the function returns True. If no rotation of b is found in a after checking all possible rotations, the function returns False.








# Solution 2:

def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd")  -> False
    cycpattern_check("hello","ell")  -> True
    cycpattern_check("whassup","psus")  -> False
    cycpattern_check("abab","baa")  -> True
    cycpattern_check("efef","eeff")  -> False
    cycpattern_check("himenss","simen")  -> True

    """
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1:] + b[:-1]
    return False

print(cycpattern_check("abcd","abd")) # False
print(cycpattern_check("hello","ell")) # True
print(cycpattern_check("whassup","psus")) # False
print(cycpattern_check("abab","baa