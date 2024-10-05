
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())


print(digitSum(""))  # 0
print(digitexact_precision_digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
print(digitSum("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # 352

This solution works by using the built-in Python function `ord` to get the ASCII code of a character, and the built-in Python function `sum` to sum up these ASCII codes. We also use the built-in Python function `isupper` to check if a character is uppercase.
"""

# 2. Write a Python function that takes a string and returns a list of tuples, where each tuple contains a character in the string and its corresponding ASCII code.

def char_to_ascii(s):
    return [(c, ord(c)) for c in s]

print(char_to_ascii("hello"))  # [('h', 104), ('e', 101), ('l', 108), ('l', 108), ('o', 111)]

# 3. Write a Python function that takes a string and returns a new string where all the uppercase letters are replaced by their corresponding lowercase letters and vice versa.

def swap_case(s):
    return "".join(c.upper() if c.islower() else c.lower() for c in s)

print(swap_case("Hello World!"))  # "hELLO wORLD!"

# 4. Write a Python function that takes a string and returns a new string with all the words reversed in the sentence.

def reverse_words(s):
    return " ".join(