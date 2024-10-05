```
def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            if char.islower():
                result += chr(ord(char) + 2)
            else:
                result += chr(ord(char) - 22)
        else:
            if char.islower():
                result += chr(ord(char) + 32)
            else:
                result += chr(ord(char) - 32)
    return result
``` 
This function goes through each character in the input message. If the character is a vowel, it shifts it by 2 places in the alphabet. If the character is not a vowel, it swaps its case. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `islower` and `isupper` functions are used to check if a character is lowercase or uppercase. 

For example, if the input is 'test', the function will return 'TGST'. The 't' is shifted by 2 places to 'v', which becomes 'T' when the case is swapped. The 'e' is shifted by 2 places to 'g', which becomes 'G' when the case is swapped. The 's' is swapped to 'S'. 

For example, if the input is 'This is a message', the function will return 'tHKS KS C MGSSCGG'. The 'T' is shifted by 2 places to 'V', which becomes 'v' when the case is swapped. The 'h' is swapped to 'H'. The 'i' is shifted by 2 places to 'k', which becomes 'K' when the case is swapped. And so on. 