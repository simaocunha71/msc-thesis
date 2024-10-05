
def encode(message):
    # Make a list of the message
    message_list = list(message)
    
    # Make a list of the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Make a list of the vowels in the message
    vowels_in_message = [v for v in message_list if v in vowels]
    
    # Make a list of the vowels in the message with the vowels moved forward 2 letters
    vowels_in_message_moved = [vowels[(vowels.index(v) + 2) % 5] for v in vowels_in_message]
    
    # Replace the vowels in the message with the vowels moved forward 2 letters
    for vowel, vowel_moved in zip(vowels_in_message, vowels_in_message_moved):
        message_list[message_list.index(vowel)] = vowel_moved
    
    # Return the encoded message
    return ''.join(message_list)
    
    # Tests
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    
    
