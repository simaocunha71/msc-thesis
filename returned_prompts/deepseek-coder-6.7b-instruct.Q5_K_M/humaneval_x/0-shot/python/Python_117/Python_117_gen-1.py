
    def select_words(s, n):
        vowels = "aeiou"
        words = s.split()
        consonants = [word for word in words if sum(1 for char in word if char.lower() not in vowels) == n]
        return consonants
    
    print(select_words("Mary had a little lamb", 4))  # ["little"]
    print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
    print(select_words("simple white space", 2))  # []
    print(select_words("Hello world", 4))  # ["world"]
    print(select_words("Uncle sam", 3))  # ["Uncle"]

This function works by splitting the input string into a list of words. Then it generates a list of words that contain exactly `n` consonants by checking the number of consonants in each word. The result is a list of words that meet the criteria.

Please note that the function is case-insensitive, as it treats all letters as lower case.

Also, this function assumes that the input string only contains letters and spaces. If there are other characters in the string, the function may not work as expected.
