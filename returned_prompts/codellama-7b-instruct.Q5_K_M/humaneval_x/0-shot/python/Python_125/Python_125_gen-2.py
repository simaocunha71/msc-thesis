
def split_words(txt):
    if txt.isalpha():
        return [txt]
    if " " in txt:
        return txt.split(" ")
    if "," in txt:
        return txt.split(",")
    count = 0
    for i in range(26):
        if txt.lower()[i] == txt.lower()[i]:
            count += 1
    return count

# Alternative 1
def split_words(txt):
    if not txt:
        return []
    if txt.isalpha():
        return [txt]
    return txt.split()

# Alternative 2
def split_words(txt):
    if not txt:
        return []
    if txt.isalpha():
        return [txt]
    return txt.split(',') or txt.split(' ')
