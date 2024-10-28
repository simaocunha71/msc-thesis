def validate(n):
    for i in str(n):
        if int(i) < len(str(n).count(i)):
            return False
    return True