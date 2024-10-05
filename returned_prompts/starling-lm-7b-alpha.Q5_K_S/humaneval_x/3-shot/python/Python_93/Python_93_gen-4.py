    vowels = set("aeiou")
    result = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                char = chr((ord(char) + 1 - ord('a')) % 26 + ord('a'))
            elif char.islower():
                char = chr((ord(char) - ord('a') + 1) % 26 + ord('Z'))
            elif char.isupper():
                char = chr((ord(char) - ord('A') + 1) % 26 + ord('a'))
        result += char
    return result


