def find_star_num(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    star_nums = [1, 13, 37, 61, 85, 109, 133, 157, 181, 205, 229, 253, 277, 301, 325, 349, 373, 397]
    return star_nums[n-1] if n <= len(star_nums) else None