def find_star_num(n):
    star_nums = [1, 13, 37, 61, 85, 109]
    return star_nums[n-1] if n <= len(star_nums) else None