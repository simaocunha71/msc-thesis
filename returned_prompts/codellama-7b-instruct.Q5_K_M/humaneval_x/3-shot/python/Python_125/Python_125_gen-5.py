    if len(txt.split(" ")) > 1:
        return txt.split(" ")
    elif len(txt.split(",")) > 1:
        return txt.split(",")
    else:
        return sum([i for i, c in enumerate(txt) if c.islower() and i % 2 != 0])


