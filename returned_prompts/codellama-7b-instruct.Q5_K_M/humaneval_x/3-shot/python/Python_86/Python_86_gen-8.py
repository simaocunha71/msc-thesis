    words = s.split()
    result = ''
    for word in words:
        new_word = ''
        for char in word:
            new_word += chr(ord(char) + 1)
        result += new_word + ' '
    return result.strip()


