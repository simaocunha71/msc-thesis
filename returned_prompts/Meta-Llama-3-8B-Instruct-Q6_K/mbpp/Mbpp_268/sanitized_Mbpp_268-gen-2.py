def find_star_num(n):
    star_nums = []
    num = 1
    while len(star_nums) < n:
        if num % 2 == 0:
            num += 1
            continue
        star = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                star = False
                break
        if star:
            star_nums.append(num)
        num += 1
    return star_nums[-1]  # Return the nth star number