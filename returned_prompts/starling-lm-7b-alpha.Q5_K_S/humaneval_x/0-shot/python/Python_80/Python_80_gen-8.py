    # Write your code here
    if len(s) < 3:
        return False
    l = []
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i+1] == s[i+2]:
            if l.count(s[i:i+3]) > 0:
                return False
        else:
            l.append(s[i:i+3])
    return True

# Time Complexity : O(n)
# Space Complexity: O(1)








# You are given a string s. Your task is to check if the string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

# For example:
# is_happy(a) => False
# is_happy(aa) => False
# is_happy(abcd) => True
# is_happy(aabb) => False
# is_happy(adb) => True
# is_happy(xyy) => False




def is_happy(s):
    # Write your code here
    if len(s) < 3:
        return False
    l = []
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i+1] == s[i+2]:
            if l.count(s[i:i+3]) > 0:
                return False
        else:
            l.append(s[i:i+3])
    return True


# Time Complexity : O(n)
# Space Complexity: O(1)








# You are given a string s. Your task is to check if the string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

# For example:
# is_happy(a) => False
# is_happy(aa) => False
# is_happy(abcd) => True
# is_happy(aabb) =>