    def encode_vowel(letter):
        if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
            return chr(ord(letter.lower()) + 1)
        else:
            return letter

    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result += encode_vowel(letter).upper()
            else:
                result += encode_vowel(letter)
        else:
            result += letter

    return result


