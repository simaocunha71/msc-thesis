    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return sum([i for i in txt if ord(i) % 2 == 0])