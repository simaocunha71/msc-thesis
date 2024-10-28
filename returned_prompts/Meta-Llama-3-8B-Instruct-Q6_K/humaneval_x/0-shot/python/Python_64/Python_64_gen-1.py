    FIX = """
    Add more test cases.
    """

    def vowels_count(s):
        s = s.lower()
        count = 0
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'y'] and (char == 'y' or s.index(char) == len(s) - 1):
                count += 1
        return count

    # Add test cases
    print(vowels_count("abcde"))  # Expected output: 2
    print(vowels_count("ACEDY"))  # Expected output: 3
    print(vowels_count("hello"))  # Expected output: 2
    print(vowels_count("aeiou"))  # Expected output: 5
    print(vowels_count("bcdfghjklmnpqrstvwxyz"))  # Expected output: 0
    print(vowels_count("AEIOUY"))  # Expected output: 5
    print(vowels_count("AEIOUy"))  # Expected output: 5
    print(vowels_count("AEIOUYy"))  # Expected output: 6
    print(vowels_count(""))  # Expected output: 0
    print(vowels_count("y"))  # Expected output: 1
    print(vowels_count("yy"))  # Expected output: 1
    print(vowels_count("yyy"))  # Expected output: 1
    print(vowels_count("yyyy"))  # Expected output: 1
    print(vowels_count("yyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyyyyyy"))  # Expected output: 1
    print(vowels_count("yyyyyyyyyyyy