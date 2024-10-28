    if a.lower().find(b.lower()) != -1:
        return True
    for i in range(1, len(b)):
        if a.lower().find(b.lower()[i:]) != -1:
            return True
    return False


