
def vowels_count(s):
    vowels = "aeiou"
    s = s.lower()
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    if s[-1] == 'y':
        count += 1
    return count

print(vowels_count("abcde"))  # should return 2
print(vowels_count("ACEDY"))  # should return 3
print(vowels_count("hello"))  # should return 2
print(vowels_count("YES"))  # should return 1
print(vowels_count("MATH"))  # should return 2
print(vowels_count("PYTHON"))  # should return 1
print(vowels_count("AUTO"))  # should return 1
print(vowels_count("BIRTHDAY"))  # should return 4
print(vowels_count("COMPUTER"))  # should return 4
print(vowels_count("PYTHONY"))  # should return 3
print(vowels_count("APPLE"))  # should return 3
print(vowels_count("GRAPH"))  # should return 2
print(vowels_count("TRAIN"))  # should return 2
print(vowels_count("PYTHON"))  # should return 1
print(vowels_count("COMPUTER"))  # should return 4
print(vowels_count("GRAPHY"))  # should return 3
print(vowels_count("BIRTHDAY"))  # should return 4
print(vowels_count("TRAIN"))  # should return 2
print(vowels_count("PYTHON"))  # should return 1
print(vowels_count("COMPUTER"))  # should return 4
print(vowels_count("GRAPHY"))  # should return 3
print(vowels_count("BIRTHDAY"))  # should return 4
print(vowels_count("TRAIN"))  # should return 2
<j