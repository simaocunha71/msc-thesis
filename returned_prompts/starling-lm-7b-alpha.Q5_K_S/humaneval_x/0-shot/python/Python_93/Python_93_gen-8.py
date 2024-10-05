
def encode(message):
    vowels = "aeiou"
    new_message = ""
    for letter in message:
        if letter.lower() in vowels:
            new_message += chr(ord(letter.upper()) + 2)
        elif letter.isupper():
            new_message += chr(ord(letter) + 32)
        elif letter.islower():
            new_message += chr(ord(letter) - 32)
        else:
            new_message += letter
    return new_message

# Code from class
# vowels = "aeiou"
# new_message = ""
# for letter in message:
#     if letter.lower() in vowels:
#         new_message += chr(ord(letter.upper()) + 2)
#     else:
#         new_message += letter
# return new_message

# print(encode('test'))
# print(encode('This is a message'))


# 