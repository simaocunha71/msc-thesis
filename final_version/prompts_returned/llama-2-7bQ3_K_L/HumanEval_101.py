
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    
    if len(s) < 1:
        return []

    words = ''
    for i in range(len(s)-1):
        for j, char in enumerate(s[i]):
            if char.isalpha() or char == ",":
                words += str(char) + ','
            elif j > 0:
                words += str(char)
    return [w for w in words[:-1]]
