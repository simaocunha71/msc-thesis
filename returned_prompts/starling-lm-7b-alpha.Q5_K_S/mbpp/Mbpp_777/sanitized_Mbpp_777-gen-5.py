def find_sum(numbers):
    sum = 0
    for i in numbers:
        if numbers.count(i) == 1:
            sum += i
    return sum