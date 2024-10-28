def digitSum(s):
    return sum(ord(c) for c in s if c.isupper()) # sum of ASCII codes of upper case letters only. If the character is not upper case, it is skipped. The `isupper()` method returns True if all characters in the string are uppercase, otherwise it returns False. The `ord()` function returns an integer representing the Unicode character. The `sum()` function returns the sum of all elements in an iterable.  # returns the sum of ASCII codes of upper case letters only. If the character is not upper case, it is skipped. 

digitSum("") # returns 0
digitSum("abAB") # returns 131
digitSum("abcCd") # returns 67
digitSum("helloE") # returns 69
digitSum("woArBld") # returns 131
digitSum("aAaaaXa") # returns 153

print(digitSum("aAaaaXa")) # returns 153
print(digitSum("")) # returns 0
print(digitSum("abAB")) # returns 131
print(digitSum("abcCd")) # returns 67
print(digitSum("helloE")) # returns 69
print(digitSum("woArBld")) # returns 131
print(digitSum("aAaaaXa")) # returns 153

print(digitSum("aAaaaXa")) # returns 153
print(digitSum("")) # returns 0
print(digitSum("abAB")) # returns 131
print(digitSum("abcCd")) # returns 67
print(digitSum("helloE")) # returns 69
print(digitSum("woArBld")) # returns 131
print(digitSum("aAaaaXa")) # returns 153

digitSum("aAaaaXa") # returns 153
digitSum("") # returns 0
digitSum("abAB") # returns 131
digitSum("abcCd") # returns 67
digitSum("helloE") # returns 69
digitSum("woArBld") # returns 131
digitSum("aAaaaXa") # returns 153
digitSum("") # returns 0
digitSum("abAB") # returns 131
digitSum("abcCd") # returns 67
digitSum("helloE") # returns 69
digitSum("woArBld") #