    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for char in text:
        if char not in vowels:
            new_string += char
    return new_string


