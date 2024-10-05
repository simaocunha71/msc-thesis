
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_text = ''

    for letter in text:
        if letter not in vowels:
            new_text += letter

    return new_text


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 5. Write a function named `capitalize_last_letter` that takes a string and returns the string with the last character capitalized.
#
# 