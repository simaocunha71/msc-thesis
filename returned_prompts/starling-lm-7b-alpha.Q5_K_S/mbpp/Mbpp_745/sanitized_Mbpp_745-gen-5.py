def divisible_by_digits(startnum, endnum):
    from math import sqrt

    # get all the numbers in the range
    all_nums = [i for i in range(startnum, endnum + 1)]

    # generate all the possible combinations of the digits of the numbers
    all_digits = set(str(i) for i in all_nums)
    all_digits = list(all_digits)

    # find the max number of digits in each combination
    max_digits = int(sqrt(len(all_digits)))

    # generate all the numbers divisible by each combination
    divisible_by_digits = []
    for i in all_digits:
        for j in all_nums:
            if j % int(i) == 0:
                divisible_by_digits.append(j)

    return divisible_by_digits