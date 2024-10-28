def find_star_num(n):
    star_nums = []
    num = 1
    while len(star_nums) < n:
        num += 1
        is_star = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_star = False
                break
        if is_star:
            star_nums.append(num)
    return star_nums[-1]