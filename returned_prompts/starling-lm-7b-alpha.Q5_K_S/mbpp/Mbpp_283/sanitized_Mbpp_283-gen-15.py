def validate(n):
    numbers = [int(i) for i in str(n)]
    return all(numbers.count(num) <= num for num in numbers)