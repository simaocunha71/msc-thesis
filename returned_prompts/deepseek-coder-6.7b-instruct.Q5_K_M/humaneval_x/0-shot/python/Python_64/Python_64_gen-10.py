
def vowels_count(s):
    vowels = 'aeiou'
    s = s.lower()
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    if s[-1] == 'y':
        count += 1
    return count

print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count("y"))  # 1
print(vowels_count(""))  # 0
print(vowels_count("qrst"))  # 0
print(vowels_count("Y"))  # 1
print(vowels_count("YEAR"))  # 2
print(vowels_count("YEARY"))  # 3
print(vowels_count(" "))  # 0
print(vowels_count("aYe"))  # 2
print(vowels_count("U"))  # 1
print(vowels_count("oU"))  # 2
print(vowels_count("IoU"))  # 3
print(vowels_count("iOUy"))  # 4
print(vowels_count("iOUY"))  # 4
print(vowels_count("quY"))  # 1
print(vowels_count("quY"))  # 1
print(vowels_count("QUY"))  # 1
print(vowels_count("quy"))  # 1
print(vowels_count("QU"))  # 1
print(vowels_count("q"))  # 0
print(vowels_count("Q"))  # 0
print(vowels_count("qrstQ"))  # 0
print(vowels_count("123"))  # 0
print(vowels_count("123y"))  # 1
print(vowels_count("!"))  # 0
print(vowels_count("!"))  # 0
print(vow