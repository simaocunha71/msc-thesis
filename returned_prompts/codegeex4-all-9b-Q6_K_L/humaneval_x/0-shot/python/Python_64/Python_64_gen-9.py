def vowels_count(s):
    vowels = "aeiou"
    s = s.lower()
    if s[-1] == "y":
        return len([c for c in s if c in vowels]) + 1
    else:
        return len([c for c in s if c in vowels])

print(vowels_count("abcde")) # 2
print(vowels_count("ACEDY")) # 3
print(vowels_count("y")) # 1
print(vowels_count("a")) # 1
print(vowels_count("A")) # 1
print(vowels_count("aeiou")) # 5
print(vowels_count("AEIOU")) # 5
print(vowels_count("aeiouy")) # 6
print(vowels_count("AEIOUY")) # 6
print(vowels_count("yaeiou")) # 5
print(vowels_count("AEIOUYy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(vowels_count("yaeiouy")) # 6
print(v