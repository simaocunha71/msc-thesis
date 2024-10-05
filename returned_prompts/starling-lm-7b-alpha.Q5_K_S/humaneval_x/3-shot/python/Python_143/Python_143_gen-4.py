    words = sentence.split()
    res = ""
    for word in words:
        if len(word) in [2,3,5,7]:
            res += word + " "
    return res.strip()


