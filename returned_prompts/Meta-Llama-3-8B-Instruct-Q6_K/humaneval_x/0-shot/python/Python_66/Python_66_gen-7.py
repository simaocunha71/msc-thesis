def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())  # using built-in functions like isupper() and ord() to solve the problem. isupper() returns True if the character is uppercase, and False if it's lowercase. ord() returns the ASCII value of a character. The sum() function is used to add up all the ASCII values. The generator expression is used to iterate over each character in the string. If the character is uppercase, its ASCII value is included in the sum. If it's lowercase, its ASCII value is ignored. The result is the sum of the ASCII values of all uppercase characters in the string.  # you can also use this way to solve the problem
    # return sum([ord(c) for c in s if c.isupper()])
    # or this way
    # return sum(ord(c) for c in s if c.upper() == c)  # check if the character is the same when converted to uppercase. If it is, it's an uppercase character.  # or this way
    # return sum(ord(c) for c in s if c.isalpha() and c[0].isupper())  # check if the character is a letter and if the first character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isalpha() and c.isupper())  # check if the character is a letter and if it's uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())  # check if the character is uppercase.  # or this way
    # return sum(ord(c) for c in s if c.isupper())