def validate(n):
    dig = str(n)
    for i in dig:
        if dig.count(i) > int(i):
            return False
    return True