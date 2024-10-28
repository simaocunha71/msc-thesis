def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))