def even_position(numbers):
    for i in range(0, len(numbers), 2):
        if numbers[i] % 2 != 0:
            return False
    return True