    s = s.replace("apples", "0").replace("oranges", "0")
    return int(s.replace("and", "").replace(" ", "")) - sum(int(i) for i in s.split() if i.isdigit()) - 1  # 1 for "and" or "and "


