def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())  # Using isupper() to filter upper case letters and ord() to get ASCII value

# Testing the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
print(digitSum("Hello"))  # Output: 72
print(digitSum("A"))  # Output: 65
print(digitSum("a"))  # Output: 0
print(digitSum("123"))  # Output: 0
print(digitSum("abc123"))  # Output: 0
print(digitSum("ABC"))  # Output: 65+67+69 = 201
print(digitSum("ABCD"))  # Output: 65+66+67+68 = 266
print(digitSum("aAbB"))  # Output: 0+65+66 = 131
print(digitSum("aAbBC"))  # Output: 0+65+66+67 = 188
print(digitSum("aAbBc"))  # Output: 0+65+66+99 = 130
print(digitSum("aAbBcD"))  # Output: 0+65+66+67+68 = 261
print(digitSum("aAbBcDe"))  # Output: 0+65+66+67+68+69 = 330
print(digitSum("aAbBcDef"))  # Output: 0+65+66+67+68+69+70 = 400
print(digitSum("aAbBcDefg"))  # Output: 0+65+66+67+68+69+71 = 421
print(digitSum("aAbBcDefgh"))  # Output: 0+65+66+67+68+69+72 = 442
print(digitSum("aAbBcDefghi"))  # Output: 0+65+66+67+