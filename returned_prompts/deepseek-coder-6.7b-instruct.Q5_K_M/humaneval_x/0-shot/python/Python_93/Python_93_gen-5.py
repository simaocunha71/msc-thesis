
    def encode(message):
        vowel_dict = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O':': Q', 'U': 'W'}
        encoded_message = ''
        for char in message:
            if char.isalpha():
                if char in vowel_dict:
                    encoded_message += vowel_dict[char]
                else:
                    encoded_message += chr(ord(char) ^ 32)
            else:
                encoded_message += char
        return encoded_message

    print(encode('test'))
    print(encode('This is a message'))

This solution works by creating a dictionary to map each vowel to its corresponding letter that appears 2 places ahead in the alphabet. It then loops through each character in the message. If the character is a letter, it replaces the vowel with the corresponding letter from the dictionary, or swaps the case of the letter if it's not a vowel. If the character is not a letter, it leaves it unchanged. 

The bitwise XOR operation with 32 is used to swap the case of the letter because the ASCII value of uppercase letters and lowercase letters differ by 32.

This solution assumes that the input message only contains letters and spaces. If the message may contain other characters, you would need to add checks to handle those cases.

Also, this solution assumes that the alphabet wraps around at the end, so 'z' becomes 'b' and 'Z' becomes 'B'. If this is not the case in your specific alphabet, you would need to modify the vowel_dict and the bitwise operation to handle the wrapping correctly.

Note: This solution is case sensitive. If you want to make it case insensitive, you can add a line to convert the message to either lower or upper case before processing it.

Note: This solution is not perfect, as it does not handle the case where 'y' or 'Y' are vowels. If you want to handle this case, you would need to modify the vowel_dict to map 'y' and 'Y' to their corresponding letter that appears