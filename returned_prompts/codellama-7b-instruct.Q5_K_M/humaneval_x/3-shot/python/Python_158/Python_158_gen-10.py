    if not words:
        return None

    unique_chars = {}
    max_unique_chars = 0
    max_word = ""

    for word in words:
        unique_chars = {}
        for char in word:
            if char not in unique_chars:
                unique_chars[char] = 1

        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            max_word = word

    return max_word


