def vowels_count(s):
    return sum(1 for c in s if c in 'aeiou' or (c == 'y' and s[-1] == c))

print(vowels_count("abcde"))
print(vowels_count("ACEDY"))