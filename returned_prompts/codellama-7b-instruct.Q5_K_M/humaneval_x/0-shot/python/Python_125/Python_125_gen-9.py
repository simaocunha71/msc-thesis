
def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.split(",")
    else:
        return sum(x for x in map(ord, txt) if x % 2)
