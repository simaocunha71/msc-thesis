    vowels = "aeiouAEIOU"
    count = 0

    for c in s:
        if c in vowels:
            count += 1

    return count

FIX = """
Add more test cases.
"""

def count_consonants(s):
    """