def find_star_num(n):
    star_nums = []
    i = 1
    while len(star_nums) < n:
        if sum(int(digit) for digit in str(i)) + 1 == i:
            star_nums.append(i)
        i += 1
    return star_nums[-1]