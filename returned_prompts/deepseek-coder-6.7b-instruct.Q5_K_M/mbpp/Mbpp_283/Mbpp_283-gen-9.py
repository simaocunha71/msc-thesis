def validate(n):
    n = str(n)
    for i in n:
        if n.count(i) > int(i):
            return False
    return True

print(validate(1234))

