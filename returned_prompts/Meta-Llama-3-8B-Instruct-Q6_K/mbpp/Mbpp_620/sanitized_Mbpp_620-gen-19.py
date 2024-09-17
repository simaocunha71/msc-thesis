def largest_subset(numbers):
    numbers.sort()
    current_sum = 0
    max_length = 0
    for num in numbers:
        if num % (current_sum + num) == 0:
            current_sum += num
            max_length += 1
        else:
            current_sum = num
            max_length = 1
    return max_length