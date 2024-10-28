def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum = 0
    prod = 1
    for num in numbers:
        sum += num
        prod *= num
    return sum, prod
