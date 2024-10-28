    encrypted_text = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + 2 + 26) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + 2 + 26) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text


