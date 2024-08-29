def find_max(words):
    """
    >>> find_max(["name", "of", 'string'])
    'string'
    >>> find_max(["name", "enam", "game"])
    'enam'
    >>> find_max(["aaaaaaa", "bb" ,"cc"])
    'aaaaaaa'
    """
    def unique_char_count(word):
        count = 0
        for c in word:
            if word.count(c) == 1:
                count += 1
        return count

    max_unique = max(unique_char_count(word) for word in words)
    max_words = [word for word in words if unique_char_count(word) == max_unique]
    return min(max_words)

if __name__ == "__main__":
    import doctest
    doctest.testmod()