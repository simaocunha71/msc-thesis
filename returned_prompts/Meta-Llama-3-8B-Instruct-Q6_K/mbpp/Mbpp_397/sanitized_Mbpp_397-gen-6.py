def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        return numbers[len(numbers)//2]  # median is the middle value if the length is odd