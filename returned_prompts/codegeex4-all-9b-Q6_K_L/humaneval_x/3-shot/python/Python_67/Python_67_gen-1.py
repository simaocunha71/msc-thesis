    s = s.replace("apples", "")
    s = s.replace("oranges", "")
    s = s.replace("and", "")
    s = s.replace(" ", "")
    s = s.replace(",", "")
    num_apples = int(s)
    num_oranges = int(s)
    num_mangoes = n - num_apples - num_oranges
    return num_mangoes

