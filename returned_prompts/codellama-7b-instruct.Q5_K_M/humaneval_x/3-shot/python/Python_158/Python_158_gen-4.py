    unique_char = {}
    max_unique = 0
    max_unique_word = ""

    for word in words:
        unique_char = {}
        unique_char_count = 0
        for char in word:
            if char not in unique_char:
                unique_char[char] = 1
                unique_char_count += 1
            else:
                unique_char[char] += 1

        if unique_char_count > max_unique:
            max_unique = unique_char_count
            max_unique_word = word

    return max_unique_word


