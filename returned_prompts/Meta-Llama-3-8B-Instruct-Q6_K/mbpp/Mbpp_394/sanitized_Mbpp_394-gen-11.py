def check_distinct(t):
    seen = set()
    for x in t:
        if x in seen:
            return False
        seen.add(x)
    return True