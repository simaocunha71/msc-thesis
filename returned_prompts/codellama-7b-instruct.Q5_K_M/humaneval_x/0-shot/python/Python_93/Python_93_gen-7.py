
def encode(message):
    # 1. Create a list of all vowels in the english alphabet
    vowels = ['a', 'e', 'i', 'o', 'u']
    # 2. Create a list of all letters in the message
    letters = [letter for letter in message]
    # 3. Create a new list of letters by replacing vowels with vowels 2 places ahead
    new_letters = []
    for i, letter in enumerate(letters):
        if letter in vowels:
            new_letters.append(vowels[(vowels.index(letter) + 2) % len(vowels)])
        else:
            new_letters.append(letter.lower() if letter.islower() else letter.upper())
    # 4. Create a new string from the list of letters
    new_string = ''.join(new_letters)
    # 5. Return the new string
    return new_string
