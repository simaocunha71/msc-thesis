    uppercase_vowels_in_even_indices = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char.isupper():
            uppercase_vowels_in_even_indices += 1
    return uppercase_vowels_in_even_indices


