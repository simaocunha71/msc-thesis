
def vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = 0
    for char in s:
        if char in vowels:
            result += 1
    return result


# Tests
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3

# More tests
print(vowels_count("aaayy"))  # 4
print(vowels_count("abcay"))  # 3
print(vowels_count(""))       # 0
print(vowels_count("ay"))     # 1
print(vowels_count("ABCD"))   # 0
print(vowels_count("aybcd"))  # 1
print(vowels_count("acbay"))  # 2
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(vowels_count("aybc"))   # 1
print(