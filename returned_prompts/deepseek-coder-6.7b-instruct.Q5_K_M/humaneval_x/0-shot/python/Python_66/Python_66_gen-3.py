
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

print(digitSum("")) #=> 0
print(digitexact_balance("abAB")) #=> 131
print(digitSum("abcCd")) #=> 67
print(digitSum("helloE")) #=> 69
print(digitSum("woArBld")) #=> 131
print(digitSum("aAaaaXa")) #=> 153

"""
Explanation:
The function `digitSum` calculates the sum of ASCII values of uppercase characters in a string `s`.
The built-in `ord` function returns the ASCII value of a character. The `isupper` function checks if a character is an uppercase letter. 
The generator expression `(ord(c) for c in s if c.isupper())` generates these ASCII values for each uppercase character in the string `s`.
The `sum` function calculates the sum of these ASCII values.
"""

"""
Test Cases:

1. digitSum("") => 0
2. digitSum("abAB") => 131
3. digitSum("abcCd") => 67
4. digitSum("helloE") => 69
5. digitSum("woArBld") => 131
6. digitSum("aAaaaXa") => 153
"""

"""
Test Cases:

1. digitSum("") => 0
2. digitSum("abAB") => 131
3. digitSum("abcCd") => 67
4. digitSum("helloE") => 69
5. digitSum("woArBld") => 131
6. digitSum("aAaaaXa") => 153
"""

"""
Test Cases:

1. digitSum("") => 0
2. digitSum("abAB") => 131
3. digitSum("abcCd") => 67
4. digitSum("helloE") => 69
5. digitSum("woArBld") => 131
6. digitSum("aAaa