def vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s.lower():
        if i in vowels:
            if i == 'y' and s[-1] != i:
                continue
            count += 1
    return count

print(vowels_count('abcde'))
print(vowels_count('ACEDY'))