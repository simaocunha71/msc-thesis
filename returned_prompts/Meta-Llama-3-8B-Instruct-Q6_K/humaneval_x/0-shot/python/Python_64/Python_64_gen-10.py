FIX = """
You can add more test cases.
"""

def vowels_count(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
# Add more test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfgh"))  # Expected output: 0
print(vowels_count("aBcDe"))  # Expected output: 3
print(vowels_count("y"))  # Expected output: 1
print(vowels_count("yY"))  # Expected output: 1
print(vowels_count("aYo"))  # Expected output: 2
print(vowels_count("aYoU"))  # Expected output: 3

