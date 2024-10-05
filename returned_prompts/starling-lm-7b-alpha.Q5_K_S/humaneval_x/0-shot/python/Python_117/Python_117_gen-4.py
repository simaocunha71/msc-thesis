
def select_words(s, n):
    """
    This function will return a list of all words from the string s that contain exactly n consonants, in order they appear in the string s.
    """

    def is_consonant(char):
        """
        This function checks if the given character is a consonant.
        """
        return char not in "aeiouAEIOU"

    def count_consonants(word):
        """
        This function counts the number of consonants in the given word.
        """
        count = 0
        for char in word:
            if is_consonant(char):
                count += 1
        return count

    words = s.split()
    selected_words = []

    for word in words:
        if count_consonants(word) == n:
            selected_words.append(word)

    return selected_words

# Example usage:
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ["world"]
print(select_words("Uncle sam", 3))  # Output: ["Uncle"]

# Here are some additional tests for the function:
print(select_words("The quick brown fox jumps over the lazy dog", 3))  # Output: ["brown", "jumps", "over"]
print(select_words("The quick brown fox jumps over the lazy dog", 2))  # Output: ["quick", "fox"]
print(select_words("The quick brown fox jumps over the lazy dog", 1))  # Output: ["The"]
print(select_words("The quick brown fox jumps over the lazy dog", 0))  # Output: []






def select_words(s, n):
    def is_consonant(char):
        return char not in