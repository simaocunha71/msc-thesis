    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split(" ")
    selected_words = []

    for word in words:
        consonant_count = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonant_count += 1
        if consonant_count == n:
            selected_words.append(word)

    return selected_words


