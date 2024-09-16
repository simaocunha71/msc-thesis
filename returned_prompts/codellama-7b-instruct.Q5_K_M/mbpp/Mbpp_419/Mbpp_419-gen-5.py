def round_and_sum(numbers):
    total=0
    for num in numbers:
        total+=round(num)
    return total*len(numbers)

