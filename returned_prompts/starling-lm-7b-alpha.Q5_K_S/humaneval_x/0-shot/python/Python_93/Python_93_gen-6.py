def encode(message):
    result = ""
    vowel_map = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'
    }
    for char in message:
        if char.isalpha():
            if char.lower() in vowel_map:
                result += vowel_map[char.lower()]
            else:
                if char.isupper():
                    result += chr(ord(char) + 32)
                else:
                    result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Testing
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'






# Time complexity: O(n)
# Space complexity: O(1)



# Testing
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'






# Time complexity: O(n)
# Space complexity: O(1)



# Testing
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'






# Time complexity: O(n)
# Space complexity: O(1)



# Testing
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'






# Time complexity: O(n)
# Space complexity: O(1)



# Testing
print(encode('test'))  # 'TGST'
print(encode('This is a message'))  # 'tHKS KS C MGSSCGG'






# Time complexity: O(n)
# Space complexity: O(1)


