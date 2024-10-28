
def validate(n):
    return all(n.count(str(i)) <= i for i in range(10))


