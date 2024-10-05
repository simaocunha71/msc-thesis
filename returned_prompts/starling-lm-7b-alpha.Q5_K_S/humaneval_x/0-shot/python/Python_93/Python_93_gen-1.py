def encode(message):
    vowels = "aeiou"
    result = ""
    for c in message:
        if c.islower():
            result += chr((((ord(c) - ord('a')) + 1) % 26) + ord('a'))
        elif c.isupper():
            result += chr((((ord(c) - ord('A')) + 1) % 26) + ord('A'))
        else:
            result += c

    for i in range(len(result)):
        if result[i] in vowels:
            result = result[:i] + chr((((ord(result[i]) - ord('a')) + 2) % 26) + ord('a')) + result[i+1:]
    return result

# def encode(message):
#     vowels = "aeiou"
#     result = ""
#     for c in message:
#         if c.islower():
#             result += chr((((ord(c) - ord('a')) + 1) % 26) + ord('a'))
#         elif c.isupper():
#             result += chr((((ord(c) - ord('A')) + 1) % 26) + ord('A'))
#         else:
#             result += c
#     for i in range(len(result)):
#         if result[i] in vowels:
#             result = result[:i] + chr((((ord(result[i]) - ord('a')) + 2) % 26) + ord('a')) + result[i+1:]
#     return result

# def encode(message):
#     vowels = "aeiou"
#     result = ""
#     for c in message:
#         if c.islower():
#             result += chr((((ord(c) - ord('a')) + 1) % 26) + ord('a'))
#         elif c.isupper():
#             result += chr((((ord(c) - ord('A')) + 1) % 26) + ord('A'))
#         else:
#             result += c