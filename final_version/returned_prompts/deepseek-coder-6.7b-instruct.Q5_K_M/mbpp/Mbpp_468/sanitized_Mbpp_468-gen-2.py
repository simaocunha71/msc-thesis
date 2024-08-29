def max_product(numbers):
    max_prod = numbers[0]
    curr_prod = numbers[0]

    for num in numbers[1:]:
        curr_prod = max(num, curr_prod * num)
        max_prod = max(max_prod, curr_prod)

    return max_prod