def find_star_num(n):
    star_nums = [1]
    i = 1
    while len(star_nums) < n:
        i += 1
        star_nums.append(i * (i + 1) // 2)
    return star_nums[-1]  # return the n'th star number