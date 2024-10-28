    if not arr:
        return None

    positive_nums = [x for x in arr if x > 0]
    negative_nums = [x for x in arr if x < 0]
    zero_nums = [x for x in arr if x == 0]

    positive_prod = 1
    for num in positive_nums:
        positive_prod *= num

    negative_prod = 1
    for num in negative_nums:
        negative_prod *= num

    zero_prod = 1
    for num in zero_nums:
        zero_prod *= num

    return sum(positive_nums) * sum(negative_nums) - sum(zero_nums) * (positive_prod + negative_prod)
