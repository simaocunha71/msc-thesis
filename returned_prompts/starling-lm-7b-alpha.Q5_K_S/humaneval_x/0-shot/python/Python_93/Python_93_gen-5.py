
def encode(message):
    """
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters, replaces all vowels in
    the message with the letter that appears 2 places ahead of that
    vowel in the english alphabet. 
    Assume only letters. 
    """
    vowels = "aeiou"
    chars = list(message)
    for i in range(len(chars)):
        if chars[i].lower() in vowels:
            index = vowels.find(chars[i].lower())
            if index == 0:
                index = 1
            chars[i] = vowels[index+2]
    for i in range(len(chars)):
        if chars[i].isupper():
            chars[i] = chars[i].lower()
        else:
            chars[i] = chars[i].upper()
    return "".join(chars)


# Test Cases
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'
print(encode('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'))  # 'BbCcDdFfGgIiKkLlNnOoPpRrSsTtUuVvWwXxYyZz'
print(encode('abcdefghijklmnopqrstuvwxyz'))  # 'cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # 'BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
print(encode('abcdefghijklmnopqrstuvwxy