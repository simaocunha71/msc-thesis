def validate(n):
    s = str(n)
    for i in s:
        if s.count(i) > int(i):
            return False
    return True

print(validate(1234))

