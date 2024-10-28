def get_ludic(num):
    res = []
    for i in range(1, num + 1):
        if is_ludic(i):
            res.append(i)
    return res
def is_ludic(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))