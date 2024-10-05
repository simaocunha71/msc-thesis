def largest_smallest_integers(lst):
    neg_nums = sorted([num for num in lst if num < 0])
    pos_nums = sorted([num for num in lst if num > 0])

    if neg_nums:
        largest_neg_num = neg_nums[-1]
    else:
        largest_neg_num = None

    if pos_nums:
        smallest_pos_num = pos_nums[0]
    else:
        smallest_pos_num = None

    return (largest_neg_num, smallest_pos_num)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))