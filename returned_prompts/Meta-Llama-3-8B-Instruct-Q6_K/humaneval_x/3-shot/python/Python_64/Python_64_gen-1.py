    def vowels_count(s):
        vowels = 'aeiou'
        count = 0
        for char in s:
            if char.lower() in vowels:
                count += 1
        return count
    FIX = """
    Add more test cases.
    """
    print(vowels_count("abcde"))  # Output: 2
    print(vowels_count("ACEDY"))  # Output: 3

    # Add more test cases
    print(vowels_count("hello"))  # Output: 2
    print(vowels_count("AEIOU"))  # Output: 5
    print(vowels_count("bcdfghjklmnpqrstvwxyz"))  # Output: 0
    print(vowels_count("AEIOUY"))  # Output: 5
    print(vowels_count("AEIOUYZ"))  # Output: 5
    print(vowels_count("AEIOUYZX"))  # Output: 5
    print(vowels_count("AEIOUYXZA"))  # Output: 5
    print(vowels_count("AEIOUYXZAB"))  # Output: 5
    print(vowels_count("AEIOUYXZABC"))  # Output: 5
    print(vowels_count("AEIOUYXZABCD"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDE"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEF"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFG"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGH"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHI"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHIJ"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHIJK"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHIJKL"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHIJKLM"))  # Output: 5
    print(vowels_count("AEIOUYXZABCDEFGHIJKLMN"))  # Output: