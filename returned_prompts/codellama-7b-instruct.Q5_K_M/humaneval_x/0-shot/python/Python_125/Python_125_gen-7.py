
def split_words(txt):
    if len(txt.split()) > 0:
        return txt.split()
    elif len(txt.split(",")) > 0:
        return txt.split(",")
    else:
        count = 0
        for i in range(26):
            if ord(chr(i + ord('a'))) in txt:
                count += 1
        return count
