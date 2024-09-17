
def validate(n):
    temp = str(n)
    for i in temp:
        if temp.count(i) > int(i):
            return False
    return True


