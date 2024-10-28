    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1])

I'm not sure what you're asking for in the last question, but here's what I think you're asking:

    def split_words(txt):
        if ' ' in txt:
            return txt.split(' ')
        elif ',' in txt:
            return txt.split(',')
        else:
            return len([char for char in txt if char.isalpha() and char.islower() and ord(char) % 2 == 1])

This function will split the input text by either spaces, commas, or characters with odd ASCII values.


A: Here are the answers:

