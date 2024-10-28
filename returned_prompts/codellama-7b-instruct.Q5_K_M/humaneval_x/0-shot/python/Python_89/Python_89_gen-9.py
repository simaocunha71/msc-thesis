
def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in s:
        if letter in alphabet:
            i = alphabet.index(letter)
            i = i + 2*2
            result += alphabet[i]
        else:
            result += letter
    return result


