def unique_product(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    product = 1
    for num, count in count_dict.items():
        product *= num ** count
    return product