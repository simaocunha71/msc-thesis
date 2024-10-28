def sum_of_digits(numbers):
    return [sum(map(int,str(num))) for num in numbers]