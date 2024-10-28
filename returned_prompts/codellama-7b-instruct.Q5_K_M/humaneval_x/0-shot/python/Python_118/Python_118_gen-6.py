
    # find all the vowels in the word
    vowels = ["a", "e", "i", "o", "u"]
    vowel_list = [char for char in word if char.lower() in vowels]

    # check if the first vowel is the closest vowel
    if vowel_list:
        first_vowel = vowel_list[0]
        if first_vowel.islower():
            return first_vowel.upper()
        elif first_vowel.isupper():
            return first_vowel.lower()
    else:
        return ""

    # check if the last vowel is the closest vowel
    if vowel_list:
        last_vowel = vowel_list[-1]
        if last_vowel.islower():
            return last_vowel.upper()
        elif last_vowel.isupper():
            return last_vowel.lower()
    else:
        return ""

    # find the closest vowel between the consonants
    for index, char in enumerate(word):
        # check if the char is a consonant
        if char.isalpha() and not char.islower():
            # check if the next char is a vowel
            if index+1 < len(word) and word[index+1].lower() in vowels:
                return word[index+1]
        # check if the char is a vowel
        elif char.isalpha() and char.lower() in vowels:
            # check if the previous char is a consonant
            if index-1 >= 0 and not word[index-1].isalpha():
                return char

    return ""
