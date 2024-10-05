
def encode(message):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += chr(ord(letter) - 32)
            else:
                encoded_message += chr(ord(letter) + 32)
            if letter in "aeiouAEIOU":
                encoded_message = encoded_message[:-1] + chr(ord(letter) + 1)
    return encoded_message

def test_encode():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    print("All tests passed.")

test_encode()




def encode(message):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += chr(ord(letter) - 32)
            else:
                encoded_message += chr(ord(letter) + 32)
            if letter in "aeiouAEIOU":
                encoded_message = encoded_message[:-1] + chr(ord(letter) + 1)
    return encoded_message

def test_encode():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    print("All tests passed.")

test_encode()




def encode(message):
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += chr(ord(letter) - 32)
            else:
                encoded_message += chr(ord(letter) + 32)
            if letter in "aeiouAEIOU":
                encoded_message = encoded_message[:-1] + chr(ord(letter) + 1)
    return encoded_message

def test_encode():
    assert encode('test') == 'TGST'
    assert encode('This is a