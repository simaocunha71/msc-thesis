
def digits(n):
    result = 1
    for i in str(n):
        if int(i) % 2 == 1:
            result *= int(i)
    return result
