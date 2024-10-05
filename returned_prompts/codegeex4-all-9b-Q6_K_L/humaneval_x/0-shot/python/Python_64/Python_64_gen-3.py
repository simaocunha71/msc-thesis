def vowels_count(s):
    vowels = "aeiou"
    if s[-1] == "y":
        return sum([1 for c in s if c in vowels]) + 1
    else:
        return sum([1 for c in s if c in vowels])

print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3