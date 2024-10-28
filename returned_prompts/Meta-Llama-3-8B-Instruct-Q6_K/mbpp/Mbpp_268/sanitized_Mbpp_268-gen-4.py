def find_star_num(n):
    star_num = 0
    i = 1
    while True:
        star_num += i
        i += 1
        if star_num % 2 != 0:
            n -= 1
            if n == 0:
                return star_num
        if n == 0:
            return star_num - i + 1
        star_num -= i
        i += 1