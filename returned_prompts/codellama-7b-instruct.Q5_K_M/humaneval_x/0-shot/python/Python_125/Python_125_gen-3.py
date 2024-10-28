
def split_words(txt):
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return sum(ord(c) < ord(c.lower()) for c in txt)
