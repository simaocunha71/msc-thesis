def find_star_num(n: int) -> int:
    star_num = 0
    for i in range(1, n+1):
        star_num += 5*(i-1)
    return star_num

