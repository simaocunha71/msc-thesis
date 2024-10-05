    vowels = ["a", "e", "i", "o", "u"]

    text = text.lower()

    for vowel in vowels:
        text = text.replace(vowel, "")

    return text


