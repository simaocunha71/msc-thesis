
def validate(n):
    return all(str(n).count(str(i)) <= i for i in range(10))


