def largest_subset(numbers):
    numbers.sort()
    max_size = 0
    for i in range(len(numbers)):
        curr_num = numbers[i]
        curr_size = 1
        for j in range(i+1, len(numbers)):
            if numbers[j] % curr_num == 0:
                curr_size += 1
        if curr_size > max_size:
            max_size = curr_size
    return max_size