def dif_Square(number):
    for i in range(1, number):
        for j in range(i, number):
            if i*i - j*j == number:
                return True
    return False