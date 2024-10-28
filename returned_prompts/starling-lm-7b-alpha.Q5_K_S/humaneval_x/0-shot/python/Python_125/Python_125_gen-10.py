
def split_words(txt):
    whitespace_found = False
    for char in txt:
        if char == " ":
            whitespace_found = True
            break
    if whitespace_found:
        return txt.split(" ")
    else:
        comma_found = False
        for char in txt:
            if char == ",":
                comma_found = True
                break
        if comma_found:
            return txt.split(",")
        else:
            count = 0
            for char in txt:
                if ord(char) % 2 != 0:
                    count += 1
            return count

# Alternate solution
def split_words(txt):
    return [s.strip() for s in txt.split(",") if s.strip()] if "," in txt else [s for s in txt if ord(s) % 2 != 0]

# Python 3.6+ solution
def split_words(txt):
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return [s for s in txt if ord(s) % 2 != 0]

# Python 3.8+ solution
def split_words(txt):
    return [s for s in txt if s != ""] if " " in txt or "," in txt else [s for s in txt if ord(s) % 2 != 0]

# Using regular expressions
import re
def split_words(txt):
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return [s for s in txt if re.match("a|b|d|e|g|h|j|k|m|n|p|q|r|t|v|w|x|y|z", s)]

# Using built-in functions
def split_words(txt):
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return [s for s in