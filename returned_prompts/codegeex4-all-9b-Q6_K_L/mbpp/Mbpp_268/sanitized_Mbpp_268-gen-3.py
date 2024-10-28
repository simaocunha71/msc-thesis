def find_star_num(n):
    def star_num(n):
        return n * (n + 1) // 2

    count = 0
    num = 1
    while count < n:
        count += 1
        num += 1
    return star_num(num)