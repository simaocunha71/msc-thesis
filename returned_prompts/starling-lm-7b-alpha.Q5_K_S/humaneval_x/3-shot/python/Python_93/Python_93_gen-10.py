    def is_vowel(letter):
        return letter in 'aeiou'

    def next_letter(letter):
        return chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))

    def swap_case(letter):
        if letter.islower():
            return letter.upper()
        else:
            return letter.lower()

    result = ''
    for letter in message:
        if is_vowel(letter):
            result += next_letter(letter)
        else:
            result += swap_case(letter)
    return result


