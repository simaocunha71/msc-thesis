
def get_closest_vowel(word):
    """
    Get the closest vowel to the right side of the word.

    Args:
        word (str): A word to find the closest vowel from.

    Returns:
        str: The closest vowel.
    """
    # find the rightmost vowel
    vowel_index = -1
    for i, char in enumerate(reversed(word)):
        if char in "aeiouAEIOU":
            vowel_index = len(word) - i
            break

    # find the closest vowel
    if vowel_index == -1:
        return ""
    else:
        return word[vowel_index]