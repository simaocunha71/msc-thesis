def two_unique_nums(numbers):
    unique_nums = []
    for i in numbers:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums