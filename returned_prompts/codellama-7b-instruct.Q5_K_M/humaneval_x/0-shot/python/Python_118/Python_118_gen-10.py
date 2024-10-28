
def get_closest_vowel(word):
    """
    Time: O(n)
    Space: O(1)
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if i < len(word) - 1 and word[i + 1] in vowels:
                continue
            if i == len(word) - 1:
                return ''
            return word[i + 1]
    return ''