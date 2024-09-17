def count_char_position(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for char in s:
        if char.lower() in alphabet:
            if char.lower() == alphabet[alphabet.index(char.lower())]:
                count += 1
    return count