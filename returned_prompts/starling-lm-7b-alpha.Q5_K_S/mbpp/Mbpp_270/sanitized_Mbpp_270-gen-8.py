def sum_even_and_even_index(numbers):
    result = 0
    for i in range(len(numbers)):
        if i % 2 == 0 and numbers[i] % 2 == 0:
            result += numbers[i]
    return result