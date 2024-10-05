    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    for c in s.lower():
        if c in vowels:
            count += 1

    return count

FIX = """
Add more test cases.
"""

