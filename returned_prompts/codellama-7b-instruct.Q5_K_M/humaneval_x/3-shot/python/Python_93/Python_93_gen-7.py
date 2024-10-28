    def vowel_swap(vowel_pos):
        return chr((ord(vowel_pos) + 2) % 26 + ord('a'))

    def non_vowel_swap(char):
        return chr((ord(char) + 1) % 26 + ord('a'))

    message = message.lower()
    new_message = ''

    for char in message:
        if char.isalpha():
            if char.islower():
                if char in 'aeiou':
                    new_message += vowel_swap(char)
                else:
                    new_message += non_vowel_swap(char)
            else:
                if char in 'AEIOU':
                    new_message += vowel_swap(char)
                else:
                    new_message += non_vowel_swap(char)
        else:
            new_message += char

    return new_message


