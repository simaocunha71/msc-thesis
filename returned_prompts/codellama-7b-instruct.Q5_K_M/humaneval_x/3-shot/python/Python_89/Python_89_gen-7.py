    def rot(letter):
        if letter.isalpha():
            return chr((ord(letter) + 2*2 - ord('a')) % 26 + ord('a'))
        else:
            return letter

    return ''.join([rot(letter) for letter in s])


