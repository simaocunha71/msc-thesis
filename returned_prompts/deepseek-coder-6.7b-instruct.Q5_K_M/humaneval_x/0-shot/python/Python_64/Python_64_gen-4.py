
def vowels_count(s):
    count = 0
    for letter in s:
        if letter.lower() in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1
    return count


print(vowels_count("abcde"))
print(vowels_count("ACEDY"))

# Output:
# 2
# 3


