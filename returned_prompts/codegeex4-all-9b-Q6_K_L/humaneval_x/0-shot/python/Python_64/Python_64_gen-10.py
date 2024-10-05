def vowels_count(s):
    s = s.lower()
    count = 0
    for char in s:
        if char in "aeiou" and char != "y":
            count += 1
        elif char == "y" and s[-1] == "y":
            count += 1
    return count

print(vowels_count("abcde"))
print(vowels_count("ACEDY"))
print(vowels_count("y"))
print(vowels_count("yummy"))
print(vowels_count("yummyy"))