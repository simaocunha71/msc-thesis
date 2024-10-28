def vowels_count(s):
    vowels = 'aeiou'
    return sum(1 for c in s.lower() if c in vowels)

print(vowels_count("abcde")) # 2
print(vowels_count("ACEDY")) # 3
print(vowels_count("Y")) # 1
print(vowels_count("")) # 0
print(vowels_count("aeiouy")) # 6
print(vowels_count("aeiouyaeiouy")) # 12

print(vowels_count("apple")) # 2
print(vowels_count("banana")) # 3
print(vowels_count("cherry")) # 2
print(vowels_count("date")) # 1
print(vowels_count("elderberry")) # 4
print(vowels_count("fig")) # 1
print(vowels_count("grape")) # 2
print(vowels_count("honeydew")) # 3
print(vowels_count("ice cream")) # 3
print(vowels_count("jelly")) # 2
print(vowels_count("kiwi")) # 2
print(vowels_count("lemon")) # 2
print(vowels_count("mango")) # 2
print(vowels_count("nectarine")) # 4
print(vowels_count("orange")) # 3
print(vowels_count("papaya")) # 3
print(vowels_count("quince")) # 2
print(vowels_count("raspberry")) # 4
print(vowels_count("strawberry")) # 3
print(vowels_count("tomato")) # 2
print(vowels_count("ugli fruit")) # 2
print(vowels_count("victoria sponge")) # 5
print(vowels_count("watermelon")) # 4
print(vowels_count("xigua")) # 2
print(vowels_count("yam")) # 1
print(vowels_count("zebra")) # 1

print(vowels_count("applepie")) # 3
print(vowels_count("banana split")) # 4
print(vowels_count("cherry tart")) # 3
print(vowels_count("date nut")) # 2
print(vowels_count("elderberry tart")) #