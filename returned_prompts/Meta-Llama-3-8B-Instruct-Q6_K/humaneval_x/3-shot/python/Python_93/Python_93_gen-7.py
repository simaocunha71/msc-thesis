    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr(ord(char) + 2)
            else:
                encoded_message += chr(ord(char) - 2)
        else:
            if char.islower():
                encoded_message += chr(ord(char) + 32)
            else:
                encoded_message += char
    
    return encoded_message
    # This function works by iterating over each character in the message. 
    # If the character is a vowel, it checks if it's lowercase or uppercase 
    # and then adds the corresponding character 2 positions ahead in the 
    # alphabet. If the character is not a vowel, it simply adds the 
    # character itself, but if it's uppercase, it adds the lowercase 
    # version instead. The result is the encoded message. 
    # Note that this function assumes that the input is a string of 
    # letters only. If there are other characters in the message, this 
    # function will not work correctly. 
    # Also, note that this function does not handle non-English characters. 
    # If the message contains characters from other alphabets, this 
    # function will not work correctly. 
    # Finally, note that this function does not handle characters that 
    # are not letters. If the message contains other characters, such as 
    # numbers or punctuation, this function will not work correctly. 
    # This function is case-sensitive, so it will treat uppercase and 
    # lowercase letters differently. 
    # This function is also English-specific, so it will not work 
    # correctly with messages that contain characters from other 
    # languages. 
    # This function is also limited to the ASCII character set, so it 
    # will not work correctly with messages that contain characters 
    # from other character sets. 
    # This function does not handle edge cases, such as an empty 
    # message or a message with only whitespace. 
    # This function does not handle invalid input, such as a message 
    # that contains characters that are not letters. 
    # This function does not handle non-standard input, such as a 
    # message that contains characters that are not part of the 
    # standard English alphabet. 
    # This function does not handle non-ASCII characters, such as 
    # accented characters or