    def vowels_count(s):
        vowels = 'aeiouy'
        s = s.lower()
        return sum(1 for char in s if char in vowels)

    # test cases
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("a") == 1
    assert vowels_count("y") == 1
    assert vowels_count("bcdfghjklmnpqrstvwxyz") == 0
    assert vowels_count("AEIOUY") == 5
    assert vowels_count("AEIOUYabc") == 5
    assert vowels_count("AEIOUYabcABC") == 5


