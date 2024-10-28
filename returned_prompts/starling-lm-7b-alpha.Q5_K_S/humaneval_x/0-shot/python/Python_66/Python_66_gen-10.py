
def digitSum(s):
    upper_chars = filter(lambda c: c.isupper(), s)
    upper_chars_ascii = map(lambda c: ord(c), upper_chars)
    return sum(upper_chars_ascii)

# Alternative solution using list comprehension
def digitSum(s):
    upper_chars = [c for c in s if c.isupper()]
    upper_chars_ascii = [ord(c) for c in upper_chars]
    return sum(upper_chars_ascii)

# Alternative solution using list comprehension and sum() function
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())


# Here are some tests for the function
assert(digitSum("") == 0)
assert(digitSum("abAB") == 131)
assert(digitSum("abcCd") == 67)
assert(digitSum("helloE") == 69)
assert(digitSum("woArBld") == 131)
assert(digitSum("aAaaaXa") == 153)
print("All tests passed!")





# Here are some tests for the function
assert(digitSum("") == 0)
assert(digitSum("abAB") == 131)
assert(digitSum("abcCd") == 67)
assert(digitSum("helloE") == 69)
assert(digitSum("woArBld") == 131)
assert(digitSum("aAaaaXa") == 153)
print("All tests passed!")





# Here are some tests for the function
assert(digitSum("") == 0)
assert(digitSum("abAB") == 131)
assert(digitSum("abcCd") == 67)
assert(digitSum("helloE") == 69)
assert(digitSum("woArBld") == 131)
assert(digitSum("aAaaaXa") == 153