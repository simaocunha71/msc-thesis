def mul_even_odd(numbers):
    even_product = 1
    odd_product = 1

    for num in numbers:
        if num % 2 == 0:
            even_product *= num
        elif num % 2 == 1:
            odd_product *= num

    product = even_product * odd_product
    return product