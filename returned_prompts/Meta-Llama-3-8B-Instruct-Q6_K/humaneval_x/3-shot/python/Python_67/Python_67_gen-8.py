    s = s.replace(" apples and ", " ")
    s = s.replace(" oranges", "")
    s = s.replace(" apples", "")
    s = s.replace(" and ", " ")
    n = int(s)
    return n - len(s.split()) + 1


