
def consonant_ctr(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() not in vowels and char.isalpha():
            count += 1
    return count

print(consonant_ctr('program2bedone'))

# Output: 8


"""
Write a python function to check if