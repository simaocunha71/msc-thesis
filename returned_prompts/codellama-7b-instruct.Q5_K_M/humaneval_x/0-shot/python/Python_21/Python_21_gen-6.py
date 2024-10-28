    import math
    sorted_nums = sorted(numbers)
    min_num = sorted_nums[0]
    max_num = sorted_nums[-1]
    range_num = max_num - min_num
    rescaled_nums = [float(num - min_num) / range_num for num in sorted_nums]
    return rescaled_nums