
def digitSum(s):
    return sum(ord(ch) for ch in s if ch.isupper())

print(digitSum("")) # 0
print(digitexactSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
print(digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) # 9415
print(digitSum("abcdefghijklmnopqrstuvwxyz")) # 0

Explanation:

The function digitSum takes a string s as input. 

It returns the sum of the ASCII codes of all uppercase characters in the string.

The sum function is used to add up all the ASCII codes.

The ord function is used to get the ASCII code of a character.

The isupper function is used to check if a character is uppercase.

This function will return 0 if there are no uppercase characters in the string.

This function will return the sum of the ASCII codes of all uppercase characters in the string.

The function will work correctly for any string of characters.
"""

# Code ends here


# Code starts from here
def digitSum(s):
    return sum(ord(ch) for ch in s if ch.isupper())

print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
print(digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) # 9415
print(digitSum("abcdefghijklmnopqrstuvwxyz")) # 0
# Code