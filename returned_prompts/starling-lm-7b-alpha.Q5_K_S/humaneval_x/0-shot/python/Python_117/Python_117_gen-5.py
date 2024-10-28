
def is_consonant(ch):
    """
    Returns True if the given character is a consonant, and False otherwise.
    """
    vowels = 'aeiou'
    if ch in vowels:
        return False
    else:
        return True

def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    """
    words = s.split()
    result = []
    for word in words:
        count = 0
        for ch in word:
            if is_consonant(ch):
                count += 1
        if count == n:
            result.append(word)
    return result

# Test
print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))    # []
print(select_words("Hello world", 4))           # ["world"]
print(select_words("Uncle sam", 3))             # ["Uncle"]


























































































































































































































