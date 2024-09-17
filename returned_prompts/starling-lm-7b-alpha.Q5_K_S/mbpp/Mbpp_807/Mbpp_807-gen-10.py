
def first_odd(numbers:list) -> int:
    for num in numbers:
        if num % 2 != 0:
            return num
    return None


