
def select_words(s, n):
    # Split s into a list of words
    words = s.split()
    # Create an empty list to store the selected words
    selected_words = []
    # Iterate over the words
    for word in words:
        # Count the number of consonants in the word
        consonant_count = 0
        for letter in word:
            if letter.isalpha() and not letter.isalpha():
                consonant_count += 1
        # Check if the word contains exactly n consonants
        if consonant_count == n:
            selected_words.append(word)
    # Return the selected words
    return selected_words


