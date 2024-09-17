def check_distinct(t):
    found_duplicate = False
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                found_duplicate = True
                break
        if found_duplicate:
            break
    return found_duplicate