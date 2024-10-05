    encoded = ""
    for c in message:
        if c.isalpha():
            if c.lower() in 'aeiou':
                if c.islower():
                    encoded += chr(ord(c) + 2)
                else:
                    encoded += chr(ord(c) + 2).upper()
            else:
                if c.islower():
                    encoded += c.upper()
                else:
                    encoded += c.lower()
        else:
            encoded += c
    return encoded


