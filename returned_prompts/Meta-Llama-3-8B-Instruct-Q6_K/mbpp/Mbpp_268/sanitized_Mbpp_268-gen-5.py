def find_star_num(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    star_num = 0
    num = 0
    while True:
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num
        if star_num % n == 0:
            return num
        star_num -= num
        num += 1
        star_num += num