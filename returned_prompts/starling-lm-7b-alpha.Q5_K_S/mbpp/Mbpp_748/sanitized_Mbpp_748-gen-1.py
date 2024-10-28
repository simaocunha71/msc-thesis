def capital_words_spaces(s):
    # First, we define a list of all capital letters
    capital_letters = [chr(x) for x in range(65, 91)]
    # Then we iterate over the string, and if the first letter of the word is a capital letter,
    # we add a space before the word
    result = ""
    prev_capital = False
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            result += s[i]
        elif capital_letters.__contains__(s[i]):
            result += " " + s[i]
        else:
            result += s[i]
            prev_capital = True
    return result