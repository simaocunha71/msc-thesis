
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    
    if len(s) < 3:
        return False
        
    n = ""
    for i in range(len(s)-2):
        r = ord(s[i]) - 97
        c = ord(s[i+1]) - 97
        d = ord(s[i+2]) - 97
        
        if (r == c) or (c == d):
            n += chr(r + 32)
            
    return not (n in s for x in range(len(s)))
    
def check_if_happy(s, i, j, k):
    """You are given a string and three integers, which represent the index of each of the three characters to be checked.
    Your task is to check if those three consecutive characters are distinct or not.
    For example:
    (a[0], a[1], a[2]) => False
    (a[0] + 1, a[1], a[2]) => True
    """
    
    r = ord(s[i]) - 97
    c = ord(s[j]) - 97
    d = ord(s[k]) - 97
    
    return (r == c or r == d or c == d)
