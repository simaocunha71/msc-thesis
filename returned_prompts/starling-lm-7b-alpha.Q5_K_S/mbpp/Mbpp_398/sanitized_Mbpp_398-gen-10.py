def sum_of_digits(numbers):
    # Your code here
    result = 0
    for i in numbers:
        result += sum(map(int, str(i)))
    return result