    def encode_vowel(char):
        vowels = "aeiou"
        if char.lower() in vowels:
            return chr(ord(char.lower()) + 2)
        else:
            return char

    def encode_case(char):
        if char.isupper():
            return char.lower()
        elif char.islower():
            return char.upper()
        else:
            return char

    result = ""
    for char in message:
        result += encode_case(char)
        result += encode_vowel(char)

    return result


