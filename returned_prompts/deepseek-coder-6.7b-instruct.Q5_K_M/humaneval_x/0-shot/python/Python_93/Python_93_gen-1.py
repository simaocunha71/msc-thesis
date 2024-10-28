
def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    new_message = []
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message.append(vowels[char])
            else:
                new_message.append(char.swapcase())
        else:
            new_message.append(char)
    return "".join(new_message)

print(encode('test'))
print(encode('This is a message'))

def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    return "".join(vowels[char] if char in vowels else char.swapcase() for char in message)

print(encode('test'))
print(encode('This is a message'))

def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    return "".join(vowels.get(char, char.swapcase()) for char in message)

print(encode('test'))
print(encode('This is a message'))

All these functions return the same output. They all take a string and encode it by swapping case of all letters and replacing all vowels with the corresponding character in the english alphabet that appears 2 places ahead.



def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G',