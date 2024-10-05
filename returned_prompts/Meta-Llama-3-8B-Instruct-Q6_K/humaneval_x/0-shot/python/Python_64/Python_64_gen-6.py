    # FIX: 
    def vowels_count(s):
        s = s.lower()
        vowels = 'aeiou'
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count

    # Additional test cases
    print(vowels_count("abcde"))  # Expected output: 2
    print(vowels_count("ACEDY"))  # Expected output: 3
    print(vowels_count("aeiou"))  # Expected output: 5
    print(vowels_count("bcdfgh"))  # Expected output: 0
    print(vowels_count("aey"))  # Expected output: 3
    print(vowels_count("xyz"))  # Expected output: 0
    print(vowels_count("AEIOU"))  # Expected output: 5
    print(vowels_count("bcefgh"))  # Expected output: 0
    print(vowels_count("aeiouAEIOU"))  # Expected output: 10
    print(vowels_count("abcdefghijklmnopqrstuvwxyz"))  # Expected output: 5
    print(vowels_count("bcdfghjklmnpqrstvwxyz"))  # Expected output: 0
    print(vowels_count("AEIOUbcdfghjklmnpqrstvwxyz"))  # Expected output: 5
    print(vowels_count("aeybcdfghjklmnpqrstvwxyz"))  # Expected output: 3
    print(vowels_count("bcdfghjklmnpqrstvwxyzAEIOU"))  # Expected output: 0
    print(vowels_count("aeybcdfghjklmnpqrstvwxyzAEIOU"))  # Expected output: 3
    print(vowels_count("AEIOUbcd"))  # Expected output: 0
    print(vowels_count("aeiouy"))  # Expected output: 5
    print(vowels_count("aey"))  # Expected output: 2
    print(vowels_count("AEIOUy"))  # Expected output: 5
    print(vowels_count("aeyAEIOU"))  # Expected output: 3
    print(vowels_count("AEIOUaeiou"))  # Expected output: 10
    print(vowels_count("