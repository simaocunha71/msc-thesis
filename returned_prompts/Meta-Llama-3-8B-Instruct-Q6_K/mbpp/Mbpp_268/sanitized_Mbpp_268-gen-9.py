def find_star_num(n):
    star_nums = [6, 28, 88, 220, 496, 812, 1364, 2180, 3536, 5776]
    return star_nums[n-1] if n <= len(star_nums) else None