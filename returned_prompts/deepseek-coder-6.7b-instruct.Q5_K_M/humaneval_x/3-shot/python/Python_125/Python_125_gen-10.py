    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        return sum([1 for ch in txt if ch.islower()]) % 2


