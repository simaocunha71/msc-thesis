
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += chr((ord(char)+2)%26 + ord('A') if char.isupper() else (ord(char)+2)%26 + ord('a'))
            else:
                encoded_message += chr((ord(char)+2)%26 + ord('A') if char.isupper() else (ord(char)+2)%26 + ord('a'))
        else:
            encoded_message += char
    return encoded_message

print(encode('test'))
print(encode('This is a message'))
print(encode('Qwertyuiopasdfghjklzxcvbnm'))
<jupyter_output>
TGST
tHKS KS C MGSSCGG
Rwfvsjylbcplkdghm
<jupyter_text>
Question 3
<jupyter_code>
