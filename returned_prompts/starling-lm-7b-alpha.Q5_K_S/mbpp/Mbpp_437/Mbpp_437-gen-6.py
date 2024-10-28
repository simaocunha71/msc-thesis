
def remove_odd(word):
    even = ""
    for char in word:
        if int(char) % 2 == 0:
            even += char
    return even


