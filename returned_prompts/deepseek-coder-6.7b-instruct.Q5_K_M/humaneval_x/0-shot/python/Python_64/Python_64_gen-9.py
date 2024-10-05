
def vowels_count(s):
    vowels = "aeiou"
    count = 0
    for letter in s:
        if letter.lower() in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

print(vowels_count("abcde"))
print(vowels_count("ACEDY"))
print(vowels_count(""))
print(vowels_count("y"))
print(vowels_count("Y"))
print(vowels_count("exquisite"))
print(vowels_count("EXquisite"))
print(vowels_count("exquisiteY"))
print(vowels_count("EXquisiteY"))
print(vowels_count("exquisitey"))
print(vowels_count("EXquisitey"))
print(vowels_count("exquisiteyY"))
print(vowels_count("EXquisiteyY"))
print(vowels_count("exquisiteyy"))
print(vowels_count("EXquisiteyy"))
print(vowels_count("exquisiteyyY"))
print(vowels_count("EXquisiteyyY"))
<jupyter_output>
2
3
0
1
0
4
4
4
4
4
4
4
4
4
4
4
4
<jupyter_text>
F. Examples:
<jupyter_code>
# Example 1:
print(vowels_count("abcde")) # Expected output: 2

# Example 2:
print(vowels_count("ACEDY")) # Expected output: 3

# Example 3:
print(vowels_count("")) # Expected output: 0

# Example 4:
print(vowels_count("y")) # Expected output: 1

# Example 5:
print(vowels_count("Y")) # Expected output: 1

# Example 6:
print(vowels_count("exquisite")) # Expected