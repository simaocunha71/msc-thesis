
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
    
    # base case
    if len(s) < 3: return False 
    # check every 3 chars are distinct and length must be >= 3
    if s[0] == s[-1]:
        return False
    elif s[:-1].count('x')==s.count('y') > 0:
        return False
    else:
        return True    
        
if __name__ == '__main__':
    print(is_happy("adb"))