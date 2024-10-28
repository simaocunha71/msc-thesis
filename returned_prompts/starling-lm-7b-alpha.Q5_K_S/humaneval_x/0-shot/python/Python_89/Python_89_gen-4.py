
def encrypt(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            encrypted += chr((ord(c) - 97 + 2 * 2 + 26) % 26 + 97)
        else:
            encrypted += c
    return encrypted

# Test
print(encrypt('hi'))       # lm
print(encrypt('asdfghjkl'))   # ewhjklnop
print(encrypt('gf'))       # kj
print(encrypt('et'))       # ix


# Other Solution:
def encrypt(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha():
            result += chr((ord(s[i]) - 97 + 2 * 2 + 26) % 26 + 97)
        else:
            result += s[i]
    return result

# Test
print(encrypt('hi'))       # lm
print(encrypt('asdfghjkl'))   # ewhjklnop
print(encrypt('gf'))       # kj
print(encrypt('et'))       # ix


# Other Solution:
def encrypt(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            encrypted += chr((ord(c) - 97 + 2 * 2 + 26) % 26 + 97)
        else:
            encrypted += c
    return encrypted

# Test
print(encrypt('hi'))       # lm
print(encrypt('asdfghjkl'))   # ewhjklnop
print(encrypt('gf'))       # kj
print(encrypt('et'))       # ix



# Other Solution:
def encrypt(s):
    encrypted = ""
    for c in s:
        if c.isalpha():
            encrypted += chr((ord(c) - 97 + 2 * 2 + 26) % 26 + 97)
        else:
           