
def anti_shuffle(s):
    return " ".join(sorted(s.split(), key=lambda x: "".join(sorted(x))))