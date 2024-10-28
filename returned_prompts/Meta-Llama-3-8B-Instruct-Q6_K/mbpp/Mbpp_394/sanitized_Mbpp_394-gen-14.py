def check_distinct(t):
    seen = set()
    for elem in t:
        if elem in seen:
            return False
        seen.add(elem)
    return True